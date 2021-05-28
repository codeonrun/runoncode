# runoncode

Welcome everyone to COR's django project. In our project structure, we made one static in which locate under "local" app, this static folder is where you can store all your static images / css / other media. The home page or index page is also locate under local app.

## How to update the site

After you update the site, there are few things that you have to do in order for it to become live
```
python manage.py collectstatic
sudo systemctl restart gunicorn

```

