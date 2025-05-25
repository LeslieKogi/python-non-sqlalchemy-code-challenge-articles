class Article:
    all=[]

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise Exception("Title must be a string between 5 and 50 characters inclusive.")

        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters inclusive.")

        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if not isinstance(author,Author):
            raise Exception("The author must be an instance of Author")
        self._author=author 

    @property
    def magazine(self):
        return self._magazine 
    
    @magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be an instance of Magazine")
        self._magazine=magazine 
       

class Author:
    all=[]

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not (isinstance(name, str) and len(name)>0):
            raise Exception("Name must be a string longer than 0 characters")
        if hasattr(self,'_name'):
            raise Exception("An authors name cannot be changed after it has been set")

        self._name=name 


    def articles(self):
        return [article for article in Article.all if article.author==self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author==self]))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        categories=list(set([article.magazine.category for article in Article.all if article.author==self]))
        return categories if categories else None

class Magazine:

    all=[]

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,name):
        if not (isinstance(name,str) and 2<= len(name) <=16):
            raise Exception("name of Magazine bust be a string between 2 and 16 characters")
        self._name=name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category):
        if not (isinstance(category,str) and len(category)>0):
            raise Exception("Magazine category must be a string greatter than 0")
        self._category=category


    def articles(self):
        return [article for article in Article.all if article.magazine==self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine==self]))

    def article_titles(self):
        titles=[article.title for article in Article.all if article.magazine==self]
        return titles if titles else None
    

    def contributing_authors(self):
        from collections import Counter
        list_of_authors=[article.author for article in Article.all if article.magazine==self] 
        author_counts=Counter(list_of_authors)
        result=[author for author, count in author_counts.items() if count>2]

        return result if result else None