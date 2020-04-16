import datetime
from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm, AnonymousMethod
from wordpress_xmlrpc.methods import posts, taxonomies, media
import pprint

pp = pprint.PrettyPrinter(indent=4)

# connect to the wordpress API and return the connection object
def connect_to_wordpress_api():

        client = Client('https://geronsocial.tk/iteration-1/xmlrpc.php', 'api-user', '6o!ZiUMhd7dGkHe&rvF^7Jmn')
        return client



# add a category
'''taxes = client.call(taxonomies.GetTerms('category'))
cat = WordPressTerm()
cat.taxonomy = 'category'
cat.name = 'python category'
cat.id = client.call(taxonomies.NewTerm(cat))
pp.pprint(cat.id) 562'''


# list_library.append([final_object, data_file['Locality Name'][i] + ' Library', data_file['Categories'][i]])
def create_new_post(client, post_list):


        for post in post_list:
                newPost = WordPressPost()
                newPost.title = post[1]
                newPost.content = post[0]
                newPost.post_status = 'publish'
                newPost.terms_names = {
                'category': post[2]
                }
                newPost.thumbnail = post[3]
                
                client.call(posts.NewPost(newPost))


'''allposts = client.call(posts.GetPosts())

for post in allposts:
    print(post.id, post.title)'''

'''
id_list = []
for post in allposts:
    id_list.append(post.id)


for item in id_list:
    check = client.call(posts.DeletePost(item))
    print(str(check))'''




