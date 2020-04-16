import re
import ast

def library_prepare(data_file, template):
    # list of library to be passed to the API
    list_library = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):
        # store a copy of the theme to be edit
        temp_template = template.read()

        # insert library name
        lib_name = temp_template.replace('LIBRARY_NAME', data_file['Locality Name'][i] + ' Library')
        # insert library address
        address = lib_name.replace('add_address', data_file['Address'][i])
        # insert library suburb
        suburb_name = address.replace('add_suburb', data_file['Suburb/Town'][i])
        # insert library phone for the final edit and store it in final_object (unique info for each)
        final_object = suburb_name.replace('add_phone', data_file['Phone'][i])

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        # store all libraries as a list with category and title for the post
        list_library.append([final_object, data_file['Locality Name'][i] + ' Library', categories, 562])

    return list_library


def sport_prepare(data_file, template):
    # list of sports centers to be passed to the API

    list_sport = []

    # insert unique info for each object to the theme.
    for i in range(0, len(data_file)):
        # store a copy of the theme to be edit
        temp_template = template.read()
        center_name = temp_template.replace('sport_centre_name', data_file['Place Name'][i])

        condition = center_name.replace('add_facility_condition',
                                        str(data_file['Facility Condition'][i]) if str(data_file['Facility Condition'][i]) != 'nan' else 'No Available information')

        change_room = condition.replace('add_changerooms',
                                        str(data_file['Changerooms'][i]) if str(data_file['Changerooms'][i]) != 'nan' else 'No Available information')

        sur_type = change_room.replace('add_field_Surface',
                                       str(data_file['Field Surface Type'][i]) if str(data_file['Field Surface Type'][i]) != 'nan' else 'No Available information')

        courts = sur_type.replace('add_field_courts',
                                  str(data_file['Number of Field Courts'][i]) if str(data_file['Number of Field Courts'][i]) != 'nan' else 'No Available information')

        sport_played = courts.replace('add_sports played',
                                      str(data_file['Sports Played'][i]) if str(data_file['Sports Played'][i]) != 'nan' else 'No Available information')

        final_object = sport_played.replace('add_address',
                                            str(data_file['Address'][i]) if str(data_file['Address'][i]) != 'nan' else 'No Available information')

        # return cursor to the beginning of the file
        template.seek(0)

        # Clean category string
        categories = ast.literal_eval(data_file['Categories'][i])

        list_sport.append([final_object, data_file['Place Name'][i], categories, 570])

    return list_sport
