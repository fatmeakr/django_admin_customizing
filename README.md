# django_admin_customizing
This is a project by django and django rest framework with some small models for a tiny online shop and I concentrated on django admin customizing.

Basically database should not be with repositories and it should be in .gitignore file, but as a small project , to be able to test the staff users
Permission and superuser's , database is attached to the project.

For testing the accessibility of super users , ‍‍‍‍create a super user via python manage.py createsuperuser.
And to have staff users you can manually add an staff user , log in and test the staff's permissions.

A group is created manually in database, called 'staff' that determines the accessibility of staff users.
This project is minimal one ,so it does not develope programmatically.
But in future, it can.

And at the end, you can test the APIs via token authentication.
