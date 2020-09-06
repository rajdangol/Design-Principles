#Inversion of Control
Hollywood Principle - "Don't call us, we will call you" (LOL)

[Example code from Martin Fowler's IOC and DI page](https://www.martinfowler.com/articles/injection.html#ComponentsAndServices)
```
public interface MovieFinder {
    List findAll();
}
```
```
class MovieLister...

  private MovieFinder finder;
  public MovieLister() {
    finder = new ColonDelimitedMovieFinder("movies1.txt");
  }

 public Movie[] moviesDirectedBy(String arg) {
      List allMovies = finder.findAll();
      for (Iterator it = allMovies.iterator(); it.hasNext();) {
          Movie movie = (Movie) it.next();
          if (!movie.getDirector().equals(arg)) it.remove();
      }
      return (Movie[]) allMovies.toArray(new Movie[allMovies.size()]);
  }
```

This will tightly couple the MovieListener class to both the Interface as well as the Implementation; as we are instatiating
a concrete class in the constructor of the class.


## Dependency Injection
The basic idea of DI is to create a different object, an assembler, that populates a field in the lister class with an apt implementation for 
the finder interface.


###Types of Dependeny Injection
1. Constructor Injection (Type 3 IOC)
2. Setter Injection (Type 2 IOC)
3. Interface Injection (Type 1 IOC)





### 1. Constructor Injection
Use constructor to decide the injection of implementation to the lister class.

```
class MovieLister...
  public MovieLister(MovieFinder finder){
    this.finder = finder;
  }
```

Now instead of instatiating ColonDelimitedMovieFinder in the constructor of Lister class, we do that in a different configuration class.
```
class Configuration...
   ...
   MovieLister lister = new MovieLister(new ColonDelimitedMovieFinder("movies1.txt"));
   ...
  }
```
The configuration class can be more robust and complex.

### 2. Setter Injection
Use setter method to inject dependency.
```
class MovieLister...
  public void setFinder(MovieFinder finder){
    this.finder = finder;
  }
```
Now, to inject dependency, call the setter method of the Lister class.

### 3. Interface Injection
User interface to perform injection.
```
public interface InjectFinder{
  void injectFinder(MovieFinder finder);
  }
```
```
class MovieLister implements InjectFinder...
  public void injectFinder(MovieFinder finder){
    this.finder = finder;
  }
```
