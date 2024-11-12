Borex Installation in Django Python

>>>Installation Python
 ->https://www.python.org/downloads/

>>For Windows OS 
 -Download python  from windows store
 -Select the Python's version to download.
 -Click on the Install Now
 -Installation in Process

>>For Linux OS
 -sudo apt update
 -sudo apt install python3
	
>>>Open terminal
 -python --version
 
>>>To check pip version  
  -py -m pip --version
  -upgread pip 
  -py -m pip install --upgrade pip

>>>Installing virtualenv	
  #linux & mac os
   ->python3 -m pip install --user virtualenv
  #Windows
  ->py -m pip install --user virtualenv


>>>Create Virtual Environment
  #linux & mac os
  ->python3 -m venv environment_name
  #Windows
  ->python -m venv environment_name

>>>Activate Environment
  #Linux & mac os
  ->source environment_name/bin/activate
  #Windows
  ->environment_name\Scripts\activate
 
>>>Install Django
 #linux & mac os
 ->pip3 install django
 #Windows
 ->pip install django
 
>>>First please check Django properly Installed or not
 #Linux/macOS
 python3 -m django --version
 #Windows
 python  -m django --version

>>>Open terminal 
 -Goto project directory using cd command
 

>>>Install few libraries
->pip install django-embed-video

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': 'Your Database Name',
        'USER' : 'Database User Name',
        'PASSWORD' : 'Your Password',
        'HOST' : "Write down Host",
        'PORT' : 'Write down port',
                
    }
}
>>>To Create superuser 
->python manage.py createsuperuser
	enter username = your_username
	enter your Email Address
	enter your password
	enter your password again 
-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>To load Static Files:-
>Go to Skote/setings.py
-Add following command:-
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT= os.path.join(BASE_DIR,'assets')

>Run Command In Terminal
-python manage.py collectstatic

>>>Authentication Configuration
Windwos:-Install Package:-pip install Django-Verify-Email
Linux:-Install Package:-pip3 install Django-Verify-Email
-Goto settings.py of Main Directory

-SMTP CONFIGURATION
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True
	EMAIL_HOST_USER = '#####YOUR EMAIL ADDRESS########'
	EMAIL_HOST_PASSWORD = '#####YOUR HOST Password########'
	DEFAULT_FROM_EMAIL = '#####YOUR EMAIL ADDRESS########'
	SERVER_EMAIL = '#####YOUR EMAIL ADDRESS########'
	 



>>>To Set Default Layout
 >Goto templates/partial/base.html
 
<!--===========================================================================-->
			<!--Vertical Layout View-->
<!--===========================================================================-->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> add attribute into the body tag [data-sidebar="dark"]
		Example -> <body data-topbar="dark" data-layout="horizontal">
Step - 3 -> Comment this code {% include 'partials/horizontal-sidebar.html' %}
Step - 4 -> Uncomment this code {% include 'partials/sidebar.html' %}

						<!-- (Light Sidebar) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Remove data attribute data-sidebar="dark" body element to have light sidebar.

						<!-- (Dark Sidebar) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute data-sidebar="dark" body element to have dark sidebar.

						<!-- (Brand Sidebar) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute data-sidebar="brand" body element to have colored sidebar.


						<!-- (Compact Sidebar) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute data-sidebar-size="md" body element to have Compact sidebar.

						<!-- (Icon Sidebar) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute data-sidebar-size="sm" body element to have Icon sidebar.


						<!-- (Boxed Layout) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute  data-layout-size="boxed"  body element to have boxed layout.


						<!-- (Scollable Layout) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute data-layout-scrollable="true body element to have scrollable layout.


<!--===========================================================================-->

<!--===========================================================================-->
			<!--Horizontal Body View-->
<!--===========================================================================-->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-topbar="dark" data-layout="horizontal"]
		Example -> <body data-topbar="dark" data-layout="horizontal">
Step - 3 -> Comment this code {% include 'partials/sidebar.html' %}
Step - 4 -> Uncomment this code {% include 'partials/horizontal-sidebar.html' %}

						<!-- (Topbar Light) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attributedata-topbar="light"  body element to have light topbar and dark menubar.


						<!-- (Boxed Layout) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute  data-layout-size="boxed"  body element to have boxed layout.


						<!-- (Scollable Layout) -->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add data attribute data-layout-scrollable="true"  body element to have scrollable layout.


<!--===========================================================================-->

<!--===========================================================================-->
			<!--light/dark/RTL Mode-->
<!--===========================================================================-->
			<!--- Dark Mode --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-topbar="dark" data-layout-mode="dark" data-sidebar="dark" ] 
		Example -> <body data-topbar="dark" data-layout-mode="dark" data-sidebar="dark">

			<!--- Light Mode --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-layout-mode="light"] 
		Example -> <body data-layout-mode="light" >

			<!--- RTL Mode --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the HTML tag [lang="en" dir="rtl"] 
		Example -> <htmllang="en" dir="rtl" >


<!--===========================================================================-->
<!--===========================================================================-->
			<!-- Layout Width -->
<!--===========================================================================-->
			<!--- Fluid --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-layout-size="fluid"]
		Example -> <body data-sidebar="dark" data-layout-size="fluid" >
<!--===========================================================================-->
			<!--- Boxed --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-layout-size="boxed"]
		Example -> <body data-sidebar="dark" data-layout-size="boxed">
<!--===========================================================================-->
<!--===========================================================================-->

<!--===========================================================================-->
			<!-- Layout (Scrollbar) Position -->
<!--===========================================================================-->
			<!--- Scrollable --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-layout-scrollable="true"]
		Example -> <body data-sidebar="dark" data-layout-scrollable="true" >
<!--===========================================================================-->
			<!--- Fixed --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-layout-scrollable="false"]
		Example -> <body data-sidebar="dark" data-layout-scrollable="false">
<!--===========================================================================-->
<!--===========================================================================-->

<!--===========================================================================-->
			<!--Topbar Color Mode-->
<!--===========================================================================-->
			<!--- Light Topbar--->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-topbar="light"]
		Example -> <body data-sidebar="dark" data-topbar="light" >
<!--===========================================================================-->
			<!--- Dark Topbar--->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-topbar="dark"]
		Example -> <body data-sidebar="dark" data-topbar="dark" >
<!--===========================================================================-->
<!--===========================================================================-->

<!--===========================================================================-->
			<!--Sidebar Mode-->
<!--===========================================================================-->
<!--======================< Sidebar Color >====================================-->
			<!--- Light Sidebar --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-sidebar="light"]
		Example -> <body data-sidebar="light" >
<!--===========================================================================-->
			<!--- Dark Sidebar --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-sidebar="dark"]
		Example -> <body data-sidebar="dark"  >
<!--===========================================================================-->
			<!--- Brand Sidebar --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-sidebar="brand"]
		Example -> <body data-sidebar="brand" >
<!--===========================================================================-->
<!--======================< Sidebar Size >====================================-->
			<!--- Default Sidebar --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-sidebar-size="lg"]
		Example -> <body data-sidebar="dark" data-sidebar-size="lg" >
<!--===========================================================================-->
			<!--- Compact Sidebar --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-sidebar-size="md"]
		Example -> <body data-sidebar="dark" data-sidebar-size="md" >
<!--===========================================================================-->
			<!--- Small Sidebar --->
Step - 1 -> Goto samply\templates\partials\base.html
Step - 2 -> Add attribute into the body tag [data-sidebar-size="sm"
		Example -> <body data-sidebar="dark" data-sidebar-size="sm" >
<!--===========================================================================-->
<!--===========================================================================-->


-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>Run your project
-Windows:-python manage.py runserver
-Linux:-python3 manage.py runserver