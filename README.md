# acelrtest
# Acelr Tech Labs Pvt. Lt Test case Recived on :28-05-21

* Assumptions Made

1.) Science Nothing Mentioned about Frond end, so without using any API's
    i have directly connected to Bootstrap templates using Jinja2 templates.

2.) Not clearly mentioned about How the order can be placed.
    Does Login required to place an order or anonymous order is allowed ?

    Hence I have prepared this project with order placing system using the Username only.
    ( No Login required, but user datas will be fetched using the submitted usernames in
     the given MS-Excel sheet )

3.) Nothing mentioned about email fields and null values in the Mobile phone.
    So i choosed "username@test.com" as a default email ID.

* Other Detaills

1.) Due to the convince of Data transfering via Git for this test case, I have choosed
    DBSqlite as Database and uploaded on GitHub. the Django Superuser login details are
    Username : admin, Password : admin, Login : http://localhost:8000/admin

2.) All the components in the UI are choosed from Bootstrap for a Fast development.

3.) There is Two different App's Named User and AdminApp which used for Place and Manage
    the order respectively.

* Usage

1.) User can place order at Home page
2.) Management is possible by login to AdminApp via  url "/adminapp"
3.) All user having password set same as "admin"
4.) Accessing the admin panel is restricted to Loged users only, 
    But No User role permission is implemented (Any user can access now)
5.) Search in Customer side display Product and Seearch in Admin side
    will result users ( As per given task )
6.) As a backend development project, Not considerd on frontend / CSS styling.
    Screen short of some UI is attached in the Templates.img folder
