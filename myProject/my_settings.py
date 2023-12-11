DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'movie',
        'USER':'root',
        'PASSWORD':'rootpw',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
SECRET_KEY='django-insecure-5%_tmum16uxj$w6!hl)pdu9-@_6#y34duj7y*gfebfht4qunfo'

EMAIL = {
    'EMAIL_BACKEND'      :'django.core.mail.backends.smtp.EmailBackend', 
    'EMAIL_USE_TLS'      : True,      
    'EMAIL_PORT'         : 587,                   
    'EMAIL_HOST'         : 'smtp.gmail.com',
    'EMAIL_HOST_USER'    : 'cgb7870@gmail.com',
    'EMAIL_HOST_PASSWORD': 'qjlv kuye eymp vqut',
    'SERVER_EMAIL'       : 'cgb7870',
    'ACCOUNT_EMAIL_SUBJECT_PREFIX':'[이메일 인증]',
     
}
