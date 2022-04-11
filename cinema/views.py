from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .methods import *


#Index website

def index(request):
    if 'email' in request.session:
       del request.session['email'];
    return render(request, 'cinema/Index.html')
    
def register_owner(request):

    email = request.POST['email'];
    psswd = request.POST['psswd'];
    fname = request.POST['fname'];
    
    #1.a. Validate email is a valid email address.
    if is_valid_email(email):
       #1.b. Validate email is not already registered in the database.
       user_exists = validate_user(email);
       if not user_exists:
       
          #1.c. Validate password contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ].
          valid_password, msg_password = is_valid_password(psswd);
          
          if valid_password:
             succ = register_user(email, psswd, fname);
             mssge = "The user "+email+" has been created";
          else:
             #1.d. If any of the above is not valid, send back a meaningful response.
             context  = {'mssge':msg_password,};
             return render(request, 'cinema/error_handling.html', context)           
       else:
          #1.d. If any of the above is not valid, send back a meaningful response.
          succ = False;
          mssge = "The user "+email+" is already registered";
          context  = {'mssge':mssge,};
          return render(request, 'cinema/error_handling.html', context)
    else:
       #1.d. If any of the above is not valid, send back a meaningful response.
       mssge = "Please, write a valid email address";
       context  = {'mssge':mssge,};
       return render(request, 'cinema/error_handling.html', context)
    
    request.session.set_expiry(1200)  
    return main_menu(request);
    
def main_menu(request):
    try:
	    if 'email' not in request.session:
	    	email = request.POST['email'];
	    	psswd = request.POST['psswd'];
	    	login_ok = validate_login(email,psswd);
	    	if login_ok:
	    	   fname = login_ok.fullname;
	    	   request.session['email'] = email;
	    	   request.session['fname'] = fname;
	    	   context  = {'email':email, 'fname':fname};
	    	   request.session.set_expiry(1200)  
	    	   return render(request, 'cinema/main_menu.html', context)
	    	else:
	    	   mssge = "Wrong email or email+password combination";
	    	   context  = {'mssge':mssge,};
	    	   return render(request, 'cinema/error_handling.html', context);
	    else:
	    	email = request.session.get('email');
	    	fname = request.session.get('fname');
	    	context  = {'email':email, 'fname':fname};
	    	return render(request, 'cinema/main_menu.html', context);
    except: 
	    mssge = "Your session has expired or you are not logged in, you will be redirected to the login page";
	    context  = {'mssge':mssge,};
	    return render(request, 'cinema/error_handling.html', context)
                
     

def register_movie_form(request):
    if 'email' in request.session:
        email = request.session.get('email');
        context  = {'email':email,};
        return render(request, 'cinema/register_movie_form.html', context);
    else:
        mssge = "Your session has expired or you are not logged in, you will be redirected to the login page";
        context  = {'mssge':mssge,};
        return render(request, 'cinema/error_handling.html', context)
    
    
def register_movie_action(request):

    if 'email' in request.session:
        email = request.POST['email'];
        name     = request.POST['mname'];
        stars   = int(request.POST['mstars']);
        release  = request.POST['mrelease'];
        classpg  = request.POST['mclasspg'];
        comments = request.POST['mcomments'];
        publicp  = request.POST['mpublic'];
        succ = register_movie(email, name, stars, release, classpg, comments, publicp);
        return redirect('main_menu');
    else:
        mssge = "Your session has expired or you are not logged in, you will be redirected to the login page";
        context  = {'mssge':mssge,};
        return render(request, 'cinema/error_handling.html', context)
            
    
def list_of_movies(request):
    if 'email' in request.session:
        email  = request.session.get('email');
        movies_public  = get_public_movies(email);
        movies_private = get_owned_movies(email);
        context = {'movies_private':movies_private, 'movies_public':movies_public,};
        return render(request, 'cinema/list_of_movies.html', context);
    else:
        mssge = "Your session has expired or you are not logged in, you will be redirected to the login page";
        context  = {'mssge':mssge,};
        return render(request, 'cinema/error_handling.html', context)
        
def delete_movie_action(request, movie_id):
    if 'email' in request.session:
        del_movie = delete_movie(movie_id);
#    email  = request.session.get('email');
#    movies_public  = get_public_movies(email);
#    movies_private = get_owned_movies(email);
#    context = {'movies_private':movies_private, 'movies_public':movies_public,};
        return redirect('list_of_movies');
    else:
        return redirect('list_of_movies');
    
def update_movie_action(request, movie_id, publicp):
    if 'email' in request.session:
        upd_movie = update_movie(movie_id,publicp);
#    email  = request.session.get('email');
#    movies_public  = get_public_movies(email);
#    movies_private = get_owned_movies(email);
#    context = {'movies_private':movies_private, 'movies_public':movies_public,};
        return redirect('list_of_movies');
    else:
        return redirect('list_of_movies');

def restart_database(request):
    rd = roll_database();
    return redirect('logout');
    
    
    

