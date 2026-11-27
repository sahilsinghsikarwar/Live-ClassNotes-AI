/**
 * ClassNote AI — Unified Platform Engine
 * Handles Theme Management, Supabase Auth Guard, Teacher Profile Hydration, and Cross-Page Sync
 */

(function () {
  'use strict';

  const THEME_STORAGE_KEY = 'classnote_global_theme';
  const LEGACY_THEME_KEY = 'classnote_theme';
  const SUPABASE_URL = 'https://wzdwnyxepryutqstsiso.supabase.co';
  const SUPABASE_ANON_KEY = 'sb_publishable_tjdSpu-3rMRBLLG5e4YIqw_QVRynkgA';

  /* ==========================================================================
     THEME MANAGEMENT
     ========================================================================== */
  function getPreferredTheme() {
    try {
      const stored = localStorage.getItem(THEME_STORAGE_KEY) || localStorage.getItem(LEGACY_THEME_KEY);
      if (stored === 'light' || stored === 'dark') return stored;
    } catch (_) {}
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }

  function applyTheme(theme, animate = false) {
    if (theme !== 'light' && theme !== 'dark') theme = 'dark';
    const root = document.documentElement;

    if (animate) {
      root.classList.add('theme-transition');
    }

    if (theme === 'dark') {
      root.classList.add('dark');
      root.classList.remove('light');
      root.setAttribute('data-theme', 'dark');
    } else {
      root.classList.remove('dark');
      root.classList.add('light');
      root.setAttribute('data-theme', 'light');
    }

    // Synchronize both storage keys so login and dashboard never conflict
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
      localStorage.setItem(LEGACY_THEME_KEY, theme);
    } catch (_) {}

    // Update all theme toggle buttons across the page
    updateThemeToggleUI(theme);

    if (animate) {
      window.setTimeout(() => root.classList.remove('theme-transition'), 320);
    }

    window.dispatchEvent(new CustomEvent('classnote_theme_changed', { detail: { theme } }));
  }

  function updateThemeToggleUI(theme) {
    const isDark = theme === 'dark';

    // Update buttons matching IDs or data attributes
    const toggleBtns = document.querySelectorAll('#theme-toggle, #theme-toggle-btn, [data-cn-theme-toggle]');
    toggleBtns.forEach(btn => {
      btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      btn.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';

      // Update icon if present
      const icon = btn.querySelector('.material-symbols-outlined, #theme-icon, #theme-toggle-icon');
      if (icon) {
        icon.textContent = isDark ? 'light_mode' : 'dark_mode';
      }

      // Update label if present
      const label = btn.querySelector('#theme-label, .theme-toggle-label');
      if (label) {
        label.textContent = isDark ? 'Light Mode' : 'Dark Mode';
      }
    });
  }

  window.ClassNoteTheme = {
    get: getPreferredTheme,
    set: (t) => applyTheme(t, true),
    toggle: () => {
      const current = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
      applyTheme(current === 'dark' ? 'light' : 'dark', true);
    }
  };

  // Expose global shorthand for buttons with onclick="window.toggleClassNoteTheme()"
  window.toggleClassNoteTheme = window.ClassNoteTheme.toggle;
  window.applyClassNoteTheme = window.ClassNoteTheme.set;

  // Apply immediately upon script execution to eliminate any FOUC
  applyTheme(getPreferredTheme(), false);

  // Cross-tab storage synchronization
  window.addEventListener('storage', (event) => {
    if ((event.key === THEME_STORAGE_KEY || event.key === LEGACY_THEME_KEY) && event.newValue) {
      applyTheme(event.newValue, true);
    }
  });

  // OS preference change listener (only if user hasn't explicitly set a preference)
  try {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      const hasSaved = localStorage.getItem(THEME_STORAGE_KEY) || localStorage.getItem(LEGACY_THEME_KEY);
      if (!hasSaved) {
        applyTheme(e.matches ? 'dark' : 'light', true);
      }
    });
  } catch (_) {}

  /* ==========================================================================
     AUTHENTICATION & TEACHER IDENTITY ENGINE
     ========================================================================== */
  function getLoginUrl() {
    // Dynamically locate the login page relative to the current file
    const path = window.location.pathname;
    if (path.includes('login page') || path.endsWith('/code.html') && path.includes('login')) {
      return window.location.href;
    }
    if (path.includes('stitch_classnote_ai_platform')) {
      return new URL('../../login%20page/code.html', window.location.href).href;
    }
    return new URL('login%20page/code.html', window.location.href).href;
  }

  function getDashboardUrl() {
    if (pathIncludes('teacher_dashboard_classnote_ai')) {
      return window.location.href;
    }
    if (pathIncludes('stitch_classnote_ai_platform')) {
      return new URL('../teacher_dashboard_classnote_ai/code.html', window.location.href).href;
    }
    return new URL('stitch_classnote_ai_platform/teacher_dashboard_classnote_ai/code.html', window.location.href).href;
  }

  function pathIncludes(name) {
    return window.location.pathname.toLowerCase().includes(name.toLowerCase());
  }

  function initSupabase() {
    if (!window.supabase?.createClient) {
      console.warn('ClassNote: Supabase JS library not loaded yet.');
      return null;
    }
    if (!window.classNoteSupabase) {
      window.classNoteSupabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    }
    return window.classNoteSupabase;
  }

  async function fetchTeacherProfile(client, user) {
    if (!user || !user.id) return null;

    let profile = {
      id: user.id,
      email: user.email || '',
      full_name: '',
      department: 'Teacher Workspace',
      role: 'teacher'
    };

    // 1. Try fetching from public.teachers table
    try {
      const { data, error } = await client
        .from('teachers')
        .select('*')
        .eq('auth_user_id', user.id)
        .maybeSingle();

      if (!error && data && data.full_name) {
        profile.full_name = data.full_name.trim();
        if (data.role) profile.role = data.role;
        if (data.department) profile.department = data.department;
      }
    } catch (e) {
      console.info('ClassNote: Profile query info:', e);
    }

    // 2. Fall back to user_metadata if full_name wasn't found in table
    if (!profile.full_name) {
      const meta = user.user_metadata || {};
      const nameFromMeta = meta.full_name || meta.name || meta.display_name;
      if (nameFromMeta && typeof nameFromMeta === 'string' && nameFromMeta.trim()) {
        profile.full_name = nameFromMeta.trim();
      }
      if (meta.department) profile.department = meta.department;
    }

    // 3. Graceful fallback for missing names (Never show email as name!)
    if (!profile.full_name) {
      profile.full_name = 'Faculty Member';
    }

    return profile;
  }

  function hydrateTeacherUI(profile) {
    if (!profile) return;
    const name = profile.full_name || 'Faculty Member';
    const email = profile.email || '';
    const department = profile.department || 'Teacher Workspace';

    // 1. Welcome greetings
    document.querySelectorAll('[data-welcome-name]').forEach(el => {
      el.textContent = name;
    });

    // 2. Teacher name displays in header / menus
    document.querySelectorAll('[data-teacher-name]').forEach(el => {
      el.textContent = name;
    });

    // 3. Elements that were labeled data-teacher-email but should display the teacher's name
    document.querySelectorAll('[data-teacher-email]').forEach(el => {
      el.textContent = name;
    });

    // 4. Dedicated email displays
    document.querySelectorAll('[data-teacher-actual-email]').forEach(el => {
      el.textContent = email;
    });

    // 5. Department / role labels
    document.querySelectorAll('[data-teacher-department], [data-teacher-role]').forEach(el => {
      el.textContent = department;
    });

    // 6. Time of day greeting
    document.querySelectorAll('[data-time-greeting]').forEach(el => {
      const hour = new Date().getHours();
      el.textContent = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening';
    });

    // 7. Dynamic avatar initials
    const initials = name.split(' ').map(part => part[0]).filter(Boolean).slice(0, 2).join('').toUpperCase() || 'T';
    document.querySelectorAll('[data-teacher-initial]').forEach(el => {
      el.textContent = initials;
    });

    // Store in session for synchronous access in subsequent pages
    try {
      sessionStorage.setItem('classnote_teacher_profile', JSON.stringify(profile));
    } catch (_) {}
  }

  async function protectPage(options = {}) {
    const { onAuthenticated } = options;
    const loginUrl = getLoginUrl();

    try {
      const client = initSupabase();
      if (!client) {
        throw new Error('Supabase client failed to initialize');
      }

      const { data: { session }, error } = await client.auth.getSession();
      if (error || !session || !session.user) {
        console.warn('ClassNote: Session expired or not found. Redirecting to login.');
        window.location.replace(loginUrl);
        return null;
      }

      window.classNoteSession = session;
      window.classNoteUser = session.user;

      // Hydrate teacher profile
      const profile = await fetchTeacherProfile(client, session.user);
      window.classNoteTeacherProfile = profile;
      hydrateTeacherUI(profile);

      // Make page visible if it was hidden for auth check
      document.documentElement.style.visibility = 'visible';

      // Attach sign out event listeners
      document.querySelectorAll('#logout-btn, #classnote-logout, [data-logout-button]').forEach(btn => {
        btn.addEventListener('click', async (e) => {
          e.preventDefault();
          if (confirm('Are you sure you want to sign out of ClassNote AI?')) {
            try {
              await client.auth.signOut();
            } catch (_) {}
            sessionStorage.clear();
            window.location.replace(loginUrl);
          }
        });
      });

      // Listen for auth state changes
      client.auth.onAuthStateChange((event, newSession) => {
        if (event === 'SIGNED_OUT' || !newSession) {
          window.location.replace(loginUrl);
        }
      });

      if (typeof onAuthenticated === 'function') {
        onAuthenticated({ session, user: session.user, profile, client });
      }

      return { session, user: session.user, profile, client };
    } catch (err) {
      console.error('ClassNote: Auth guard error:', err);
      window.location.replace(loginUrl);
      return null;
    }
  }

  window.ClassNoteAuth = {
    init: initSupabase,
    protectPage,
    fetchProfile: fetchTeacherProfile,
    hydrateUI: hydrateTeacherUI,
    getLoginUrl,
    getDashboardUrl
  };

  // Run DOMContentLoaded setup
  document.addEventListener('DOMContentLoaded', () => {
    updateThemeToggleUI(getPreferredTheme());

    // Connect any theme toggle button automatically
    document.querySelectorAll('#theme-toggle, #theme-toggle-btn, [data-cn-theme-toggle]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        window.ClassNoteTheme.toggle();
      });
    });

    // Check cached profile for immediate instant rendering before network fetch
    try {
      const cached = JSON.parse(sessionStorage.getItem('classnote_teacher_profile') || 'null');
      if (cached) hydrateTeacherUI(cached);
    } catch (_) {}
  });

})();
