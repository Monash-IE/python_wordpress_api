import ast

import pandas as pd
from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm, AnonymousMethod
from wordpress_xmlrpc.methods import posts, taxonomies, media
import pprint


# size setup for pandas
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pp = pprint.PrettyPrinter(indent=4)


# connect to the wordpress API and return the connection object
def connect_to_wordpress_api():
    client = Client('https://geronsocial.tk/iteration-1/xmlrpc.php', 'api-user', '6o!ZiUMhd7dGkHe&rvF^7Jmn')
    return client



# [final_object, data_file['Locality Name'][i] + ' Library', categories, tags]
def create_new_post(client, post_list):

    # get all categories
    cats = client.call(taxonomies.GetTerms('category'))

    # Store categories in a list
    list_all_cate = []
    s_cat_id = ''

    for cat in cats:

        # store the special category id
        if str(cat) == 'special_cat':
            s_cat_id = cat.id
            print('the special_cat id is : ' + cat.id)

        list_all_cate.append(str(cat))



    # work with each post
    for post in post_list:

        # if the sub-category under the special category (special_cat) does not exit create it
        if str(post[2][-1]) not in list_all_cate:

            print('does not exist: ' + str(post[2][-1]))
            child_cat = WordPressTerm()
            child_cat.taxonomy = 'category'
            child_cat.parent = s_cat_id
            # get the last element in the category list
            child_cat.name = str(post[2][-1])
            client.call(taxonomies.NewTerm(child_cat))
            # Add the new category to the list
            list_all_cate.append(str(post[2][-1]))
        else:
            print('looking good')

        # create the post
        newPost = WordPressPost()
        newPost.title = post[1]
        newPost.content = post[0]
        newPost.post_status = 'publish'

        # check if the suburb exist in other cities
        # -- something something --

        newPost.terms_names = {
            'post_tag': post[3],
            'category': post[2]
        }
        # newPost.thumbnail = post[3]

        client.call(posts.NewPost(newPost))


# delete all post on the website
def delete_all_post(client):

        allposts = client.call(posts.GetPosts({'number': 865})) # add the number of total post on the web

        id_list = []
        for post in allposts:
            id_list.append(post.id)

        for item in id_list:
            check = client.call(posts.DeletePost(item))
            print(str(check))


# Delete all categories - IF NEEDED -
def delete_all_category(client):
    cats = client.call(taxonomies.GetTerms('category'))
    for cat in cats:
        # avoid deleting the default category
        if str(cat) != 'Default Category':
            client.call(taxonomies.DeleteTerm('category', cat.id))
            print(str(cat) + ' deleted')


# Create Categories in advance - IF NEEDED -
def create_city_suburb_categories(client):
    # open the cities files to DataFrame
    data_file = pd.read_csv('Output_files/new_Suburbs_final-2.csv')

    # get the cities with no duplication rows and convert it to list
    list_lga = data_file['Municipality'].unique().tolist()

    # loop throw the cities
    for lga in list_lga:

        # get the suburbs of each city
        suburbs = data_file[data_file['Municipality'] == lga]['Suburb'].tolist()

        # create city category as parent
        cat = WordPressTerm()
        cat.taxonomy = 'category'
        cat.name = lga
        cat.id = client.call(taxonomies.NewTerm(cat))
        print('==================================')
        print('Done City ' + lga)

        # create suburbs categories as child for each city
        for suburb in suburbs:
            child_cat = WordPressTerm()
            child_cat.taxonomy = 'category'
            child_cat.parent = cat.id
            child_cat.name = suburb
            client.call(taxonomies.NewTerm(child_cat))
            print('Done Suburb ' + suburb)


# verify the city and suburb duplication before implementation
def check_dublicat_city_or_suburb(client):

    # load categories (city and suburb)
    taxes = client.call(taxonomies.GetTerms('category'))

    # clean the return data and add them to list
    list_all_cate = []
    for taxe in taxes:
        list_all_cate.append(str(taxe))

    # open the target file to check
    data_file = pd.read_csv('Output_files/Worship_new.csv')

    # standardize the text into lower case
    data_file['Categories'] = data_file['Categories'].str.lower()

    # compare the one from the website and the target file
    for row in range(0, len(data_file)):

        city = ast.literal_eval(data_file['Categories'][row])[0]
        suburb = ast.literal_eval(data_file['Categories'][row])[1]

        if str(city) not in list_all_cate:
            print('new city=' + city +'|')

        if str(suburb) not in list_all_cate:
            print('new suburb = ' + suburb)
    print('Good Job')

def check_dublicate_post_name(client):
        posts_list = client.call(posts.GetPosts({'number': 100}))
        print(len(posts_list))
        list_all_posts = []

        for post in posts_list:
                list_all_posts.append(str(post))
        print(len(list_all_posts))



def main():

        client = connect_to_wordpress_api()
        #taxes = client.call(taxonomies.GetTerm('category',1897))
        #print(taxes.parent)


        # delete all existing categories
        #delete_all_category(client)

        # Create new Categories
        #create_city_suburb_categories(client)

        # validate datasets categories
        check_dublicat_city_or_suburb(client)

        # validate duplicate posts
        #check_dublicate_post_name(client)

        # delete all post
        #delete_all_post(client)


if __name__ == "__main__":
    main()
