import ast


# prepare library post
def library_prepare(data_file, template):
    # list of library to be passed to the API
    list_library = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):
        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert library name
        lib_name = temp_template.replace('LIBRARY_NAME', data_file['Suburb'][i] + ' Library')
        # insert library address
        address = lib_name.replace('add_address', str(data_file['Address'][i]))
        # insert library suburb
        suburb_name = address.replace('add_suburb', data_file['Suburb'][i])
        # insert library phone for the final edit and store it in final_object (unique info for each)
        final_object = suburb_name.replace('add_phone', str(data_file['Phone'][i]))

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # create the category unique name
        '''s_cat = ''
        for j in categories:
            s_cat = s_cat + j + '-'''

        # get tags (all but cities and suburbs)
        tags = categories[2:]
        categories = categories[:3]

        # add to the list of categories
        #categories.append(s_cat)

        # store all libraries as a list with category and title for the post
        list_library.append([final_object, data_file['Suburb'][i] + ' Library', categories, tags])

    return list_library


# Prepare sport posts
def sport_prepare(data_file, template):
    # list of sports centers to be passed to the API
    list_sport = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):

        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert the sport center name
        center_name = temp_template.replace('sport_centre_name', data_file['Place Name'][i])

        # insert facility condition
        condition = center_name.replace('add_facility_condition',
                                        str(data_file['Facility Condition'][i]) if str(data_file['Facility Condition'][
                                                                                           i]) != 'nan' else 'No Available information')
        # insert change room info
        change_room = condition.replace('add_changerooms',
                                        str(data_file['Changerooms'][i]) if str(
                                            data_file['Changerooms'][i]) != 'nan' else 'No Available information')

        # insert number of field available
        sur_type = change_room.replace('add_field_Surface',
                                       str(data_file['Field Surface Type'][i]) if str(
                                           data_file['Field Surface Type'][i]) != 'nan' else 'No Available information')

        # insert number of courts available
        courts = sur_type.replace('add_field_courts',
                                  str(data_file['Number of Field Courts'][i]) if str(
                                      data_file['Number of Field Courts'][i]) != 'nan' else 'No Available information')

        # insert type of sport
        sport_played = courts.replace('add_sports played',
                                      str(data_file['Sports Played'][i]) if str(
                                          data_file['Sports Played'][i]) != 'nan' else 'No Available information')

        # insert the address to the final object to be added to the list of posts
        final_object = sport_played.replace('add_address',
                                            str(data_file['Address'][i]) if str(
                                                data_file['Address'][i]) != 'nan' else 'No Available information')

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # create the category unique name
        '''s_cat = ''
        for j in categories:
            s_cat = s_cat + j + '-'''

        # get tags (all but cities and suburbs)
        tags = categories[2:3]

        # add the special category to the list of categores
        #categories.append(s_cat)

        list_sport.append([final_object, data_file['Place Name'][i], categories, tags])

    return list_sport


# Prepare tourist posts
def tourist_prepare(data_file, template):
    # list of sports centers to be passed to the API
    list_tourist = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):

        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert tourist name
        center_name = temp_template.replace('tourist_name', data_file['Place Name'][i])

        # insert historical information
        history_info = center_name.replace('add_history',
                                           str(data_file['Historical Information'][i]) if str(
                                               data_file['Historical Information'][
                                                   i]) != 'nan' else 'No Available information')

        # insert suburb
        suburb = history_info.replace('add_suburb',
                                      str(data_file['Suburb'][i]) if str(
                                          data_file['Suburb'][i]) != 'nan' else 'No Available information')

        # insert city
        city = suburb.replace('add_city',
                              str(data_file['Municipality'][i]) if str(
                                  data_file['Municipality'][i]) != 'nan' else 'No Available information')

        # insert URL
        url = city.replace('add_url',
                           str(data_file['Url'][i]) if str(
                               data_file['Url'][i]) != 'nan' else 'No Available information')

        # insert the place type to the final object to be added to the list of posts
        final_object = url.replace('add_type',
                                   str(data_file['Feature Type'][i]) if str(
                                       data_file['Feature Type'][i]) != 'nan' else 'No Available information')

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # create the category unique name
        '''s_cat = ''
        for j in categories:
            s_cat = s_cat + j + '-'''

        # get tags (all but cities and suburbs)
        tags = categories[2:]
        categories = categories[:3]

        # add the special category to the list of categories
        #categories.append(s_cat)

        list_tourist.append([final_object, data_file['Place Name'][i], categories, tags])

    return list_tourist


# Prepare nature posts
def nature_prepare(data_file, template):
    # list of sports centers to be passed to the API
    list_nature = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):

        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert tourist name
        center_name = temp_template.replace('nature_name', data_file['Place Name'][i])

        # insert historical information
        history_info = center_name.replace('add_history',
                                           str(data_file['Historical Information'][i]) if str(
                                               data_file['Historical Information'][
                                                   i]) != 'nan' else 'No Available information')

        # insert suburb
        suburb = history_info.replace('add_suburb',
                                      str(data_file['Suburb'][i]) if str(
                                          data_file['Suburb'][i]) != 'nan' else 'No Available information')

        # insert city
        city = suburb.replace('add_city',
                              str(data_file['Municipality'][i]) if str(
                                  data_file['Municipality'][i]) != 'nan' else 'No Available information')

        # insert URL
        url = city.replace('add_url',
                           str(data_file['Url'][i]) if str(
                               data_file['Url'][i]) != 'nan' else 'No Available information')

        # insert the place type to the final object to be added to the list of posts
        final_object = url.replace('add_type',
                                   str(data_file['Feature Type'][i]) if str(
                                       data_file['Feature Type'][i]) != 'nan' else 'No Available information')

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # create the category unique name
        '''s_cat = ''
        for j in categories:
            s_cat = s_cat + j + '-'''

        # get tags (all but cities and suburbs)
        tags = categories[2:]
        categories = categories[:4]

        # add the special category to the list of categories
        #categories.append(s_cat)

        list_nature.append([final_object, data_file['Place Name'][i], categories, tags])

    return list_nature


# Prepare worship posts
def worship_prepare(data_file, template):
    # list of sports centers to be passed to the API
    list_worship = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):

        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert tourist name
        center_name = temp_template.replace('worship_name', data_file['Place Name'][i])

        # insert historical information
        history_info = center_name.replace('add_history',
                                           str(data_file['Historical Information'][i]) if str(
                                               data_file['Historical Information'][
                                                   i]) != 'nan' else 'No Available information')

        # insert suburb
        suburb = history_info.replace('add_suburb',
                                      str(data_file['Suburb'][i]) if str(
                                          data_file['Suburb'][i]) != 'nan' else 'No Available information')

        # insert city
        city = suburb.replace('add_city',
                              str(data_file['Municipality'][i]) if str(
                                  data_file['Municipality'][i]) != 'nan' else 'No Available information')

        # insert the url to the final object to be added to the list of posts
        final_object = city.replace('add_url',
                                    str(data_file['Url'][i]) if str(
                                        data_file['Url'][i]) != 'nan' else 'No Available information')

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # create the category unique name
        '''s_cat = ''
        for j in categories:
            s_cat = s_cat + j + '-'''

        # get tags (all but cities and suburbs)
        tags = categories[2:3]
        categories = categories[:3]

        # add the special category to the list of categories
        #categories.append(s_cat)

        list_worship.append([final_object, data_file['Place Name'][i], categories, tags])

    return list_worship


# Prepare volunteers posts
def volunteers_prepare(data_file, template):

    # list of sports centers to be passed to the API
    list_volunteers = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):

        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert volunteer name
        center_name = temp_template.replace('Volunteer_name', data_file['Name'][i])


        # insert suburb
        suburb = center_name.replace('add_suburb',
                                      str(data_file['Suburb'][i]) if str(
                                          data_file['Suburb'][i]) != 'nan' else 'No Available information')

        # insert postcode
        postcode = suburb.replace('add_postcode',
                                      str(data_file['Postcode'][i]) if str(
                                          data_file['Postcode'][i]) != 'nan' else 'No Available information')

        # insert address
        address = postcode.replace('add_address',
                              str(data_file['Address'][i]) if str(
                                  data_file['Address'][i]) != 'nan' else 'No Available information')

        # insert the url to the final object to be added to the list of posts
        final_object = address

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # get tags (all but cities and suburbs)
        tags = categories[2:3]

        list_volunteers.append([final_object, data_file['Name'][i], categories, tags])
        print(list_volunteers)
    return list_volunteers


# Prepare clubs posts
def clubs_prepare(data_file, template):

    # list of sports centers to be passed to the API
    list_clubs = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):

        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert club name
        center_name = temp_template.replace('club_name', data_file['Place Name'][i])

        # insert time
        time = center_name.replace('add_time',
                                      str(data_file['Day'][i]) if str(
                                          data_file['Day'][i]) != 'nan' else 'No Available information')

        # insert phone
        phone = time.replace('add_phone',
                                      str(data_file['Phone Number'][i]) if str(
                                          data_file['Phone Number'][i]) != 'nan' else 'No Available information')

        # insert url
        url = phone.replace('add_url',
                                      str(data_file['URL'][i]) if str(
                                          data_file['URL'][i]) != 'nan' else 'No Available information')

        # insert description
        desc = url.replace('add_desc',
                                      str(data_file['Description'][i]) if str(
                                          data_file['Description'][i]) != 'nan' else 'No Available information')


        # insert address
        address = desc.replace('add_address',
                              str(data_file['Address'][i]) if str(
                                  data_file['Address'][i]) != 'nan' else 'No Available information')

        # insert the url to the final object to be added to the list of posts
        final_object = address

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # get tags (all but cities and suburbs)
        tags = categories[2:3]

        list_clubs.append([final_object, data_file['Place Name'][i], categories, tags])
    return list_clubs

