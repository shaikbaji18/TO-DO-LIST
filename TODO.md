# TODO List for ToDo App Modifications

- [x] Modify `todo/app/templates/base.html` to remove animations except background particles (remove glow, hover transforms, floating, interactive-element effects, button animations, etc.)
- [x] Removed "Set Due Date" button and related functionality as it was not working
- [x] Removed `set_due_date` view from `todo/app/views.py`
- [x] Removed URL pattern for `set_due_date` from `todo/todo/urls.py`
- [x] Run Django server to test changes
- [x] Fixed database column error by removing `created_at` field from `TodoList` model to match existing database schema without altering the database
