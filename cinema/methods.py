from cinema.models import Owner, Movie
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

#Validate password contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ].
def is_valid_password(psswd):    

    valid_psswd = True;
    msg_psswd   = '';
    required_chars=['!', '@', '#', '?',']'];
     
    if len(psswd) < 10:
        msg_psswd+='Password does not contain at least 10 characters 10 characters, ';
        valid_psswd = False
          
    if not any([char.islower() for char in psswd]):
        msg_psswd+='Password does not contain at least one lowercase letter, ';
        valid_psswd = False
                 
    if not any([char.isupper() for char in psswd]):
        msg_psswd+='Password does not contain at least one uppercase letter, ';
        valid_psswd = False
          
    if not any([char in required_chars for char in psswd]):
        msg_psswd+='Password does not contain at least one of the following characters: !, @, #, ? or ]';
        valid_psswd = False
    
    return valid_psswd, msg_psswd;


def is_valid_email(email):
    valid_email = True;
    try:
        validate_email(email)
    except ValidationError as e:
        valid_email=False;
        print("bad email, details:", e)
    return valid_email;

def validate_user(email):
    owner = None;
    try:
    	owner = Owner.objects.get(username=email);
    except:
        owner = False;
    return owner;

def register_user(email, psswd, fname):
    owner = Owner.objects.create(username = email, password = psswd, fullname = fname);
    owner.save();
    return True;

def validate_login(email,psswd):
    exists = validate_user(email);
    owner = True;
    if not exists:
       owner = False;
    else:
       try:
          owner = Owner.objects.get(username=email);
          psswd_ok = owner.password==psswd;
          if not psswd_ok: 
             owner = False
       except:
          owner = False;
    
    return owner;
    
def register_movie(email, name, stars, release, classpg, comments, publicp):
    owner = Owner.objects.get(username=email);
    movie = Movie.objects.create(owner=owner, name=name, stars=stars, release=release, classpg=classpg, comments=comments, publicp=publicp); 
    movie.save();
    
    return True;
    
    
def get_public_movies(email):
    public_movies = Movie.objects.filter(Q(publicp=True) & ~Q(owner__pk=email));
    return public_movies;
    
def get_owned_movies(email):
    owned_movies  = Movie.objects.filter(owner__pk=email);
    return owned_movies;
    
    
def delete_movie(movie_id):
    succ = True;
    try:
       record = Movie.objects.get(id = movie_id)
       record.delete()
    except:
       succ = False;
    return succ;

def update_movie(movie_id,publicp):
    succ = True;
    try:
       movie = Movie.objects.get(pk=movie_id);
       movie.publicp = publicp;
       movie.save();
       print(f'{publicp}');
    except:
       succ=False;
    return succ;
    
def roll_database():
    Movie.objects.all().delete()
    Owner.objects.all().delete()
    owner = Owner.objects.create(username = 'username1@email1.com', password = 'EasyKey###', fullname = 'User 1');
    owner.save();
    
    for movie in range(6):
        movie = Movie.objects.create(owner=owner, name=f'movie1{movie}', stars=5, release='2022-06-06', classpg='PG', comments=f'Nice movie {movie} - 1', publicp=True); 
        movie.save();
   

    owner = Owner.objects.create(username = 'username2@email2.com', password = 'EasyKey###', fullname = 'User 2');
    owner.save();

    for movie in range(6):
        movie = Movie.objects.create(owner=owner, name=f'movie2{movie}', stars=5, release='2022-06-06', classpg='PG', comments=f'Nice movie {movie} - 2', publicp=True); 
        movie.save();

    owner = Owner.objects.create(username = 'username3@email3.com', password = 'EasyKey###', fullname = 'User 3');
    owner.save();

    for movie in range(6):
        movie = Movie.objects.create(owner=owner, name=f'movie2{movie}', stars=5, release='2022-06-06', classpg='PG', comments=f'Nice movie {movie} - 3', publicp=True); 
        movie.save();
    
    return True;

    
#   name     = models.CharField(max_length=30);
#   stars    = models.IntegerField();
#   release  = models.DateTimeField(blank=True, null=True, default=datetime.date.today)
#   classpg  = models.CharField(max_length=5);
#   comments = models.TextField(null=True);
#   publicp  = models.BooleanField(default=True);
          
       
     
