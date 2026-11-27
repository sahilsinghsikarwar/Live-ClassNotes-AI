# ClassNote AI shared theme

Files:
- `theme.css` — shared palette and reusable component styles.
- `theme.js` — shared theme state, persistence and synchronization.

## Add to each page
Inside `<head>`:
```html
<link rel="stylesheet" href="../shared-theme/theme.css">
<script src="../shared-theme/theme.js"></script>
```
Adjust the relative path from each page to the shared-theme folder.

For the existing theme toggle button, add:
```html
data-cn-theme-toggle
```
If it has a Material Symbols icon, mark the icon:
```html
<span data-cn-theme-icon class="material-symbols-outlined">light_mode</span>
```

Set theme from code:
```js
ClassNoteTheme.set("light"); // or "dark"
ClassNoteTheme.toggle();
```

The shared controller stores the choice in `localStorage` under `classnote_global_theme`.
All pages must be served from the same origin (same host and port) to share this setting.

IMPORTANT:
This is the common theme foundation. It does not automatically map every existing custom Tailwind/class-based component to the new palette. Each page's old page-specific theme scripts/styles may need to be removed or adapted, and each existing header toggle must be connected as above. Keep backups before integrating.