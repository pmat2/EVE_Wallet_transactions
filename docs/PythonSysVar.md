# Setting python system variable
While installing python you will be asked if you want installer to set system variable for python.
<b>IF</b> you missed that point:
- locate installed python directory (e.g. C:\Users\<user>\AppData\Local\Programs\Python\Python310)
- go to "Edit the system environment variables" (e.g. win > type "system variable")
- open "Environment Variables..."
- under System variables select "Path", hit "Edit..."
- click new, then paste python directory
- Click OK on both windows

## Verify added system variable
- open terminal (win+r, type cmd, hit enter)
- in terminal type 'python', hit enter
- you should see message:
`Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.`