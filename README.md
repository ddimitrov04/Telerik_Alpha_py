<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Defining Classes Practice

It's time to practice the building blocks of a class:

- attributes - to store data
- initializers - to create classes more easily and to make sure our classes have correct data
- methods - to do something with the stored data

## 1. Attributes
Create a file `forum_post.py`
Create an empty class ForumPost
```py
class ForumPost():
    pass
```
Import the class in the `main.py` file. Create two instances of the class and assign properties to them:
```py
post1 = ForumPost()
post1.author = "Steven"
post1.text = "How to find use for every Microsoft product."
post1.upvotes = 2

post2 = ForumPost()
post2.author = "Todor"
post2.text = "Alfa Romeo for sale. Preowned by Italian grandma"
post2.upvotes = 300

print(f'{post1.text} / by {post1.author}, {post1.upvotes} votes.')
print(f'{post2.text} / by {post2.author}, {post2.upvotes} votes.')
```

If everything is allright, you should see the following output:
```none
How to find use for every Microsoft product. / by Steven, 2 votes.
Alfa Romeo for sale. Preowned by Italian grandma / by Todor, 300 votes.
```
## 2. Initializer

Freely assigning attributes to instances is valid python, but is dangerous, prone to errors, and does not scale beyond one file. Create an initializer that has the **responsibility to assign the required attributes**.
- don't forget the `self` param!
  
- `author` (str)
- `text` (str)
- `upvotes` (int)

### Test your code

If everything is done correctly, pasting the following code inside your `main` file should **run without errors** and: **produce correct output**.

#### Code

```py
post1 = ForumPost("Steven", "How to find use for every Microsoft product.", 2)
post2 = ForumPost("Todor", "Alfa Romeo for sale. Preowned by Italian grandma", 300)

print(f'{post1.text} / by {post1.author}, {post1.upvotes} votes.')
print(f'{post2.text} / by {post2.author}, {post2.upvotes} votes.')
```

#### Expected output

```none
How to find use for every Microsoft product. / by Steven, 2 votes.
Alfa Romeo for sale. Preowned by Italian grandma / by Todor, 300 votes.
```

## 3. Methods

Add a method `view()` to `ForumPost`. We can do the formatting there and not rely on _outside_ code to correctly format a post.
- don't forget the `self` param!

### Test your code

#### Code

```python
post1 = ForumPost("Steven", "How to find use for every Microsoft product.", 2)
post2 = ForumPost("Todor", "Alfa Romeo for sale. Preowned by Italian grandma", 300)


print(post1.view())
print(post2.view())
```

#### Expected output

```none
How to find use for every Microsoft product. / by Steven, 2 votes.
Alfa Romeo for sale. Preowned by Italian grandma / by Todor, 300 votes.
```

## 4. Replies

Refactor your class to support a collection of replies: 
You should create the collection as an empty list in the initializer. There is no need to accept the collection as an argument to the initializer method.


Methods:
- don't forget the `self` param!
- create an `add_reply()` method that adds a new reply to the replies collection
- refactor the `view()` method to display the replies if present.

### Test your code

#### Code

```python
post1 = ForumPost("Steven", "How to find use for every Microsoft product.", 2)
post2 = ForumPost("Todor", "Alfa Romeo for sale. Preowned by Italian grandma", 300)
post1.add_reply("I like Google!")
post1.add_reply("Ugh, Microsoft... :(")

print(post1.view())
print(post2.view())
```

#### Expected output

```none
How to find use for every Microsoft product. / by Steven, 2 votes.
- I like Google!
- Ugh, Microsoft... :(
Alfa Romeo for sale. Preowned by Italian grandma / by Todor, 300 votes.
```
