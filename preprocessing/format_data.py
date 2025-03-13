def format_language(language):

    formated_language = "NA"

    if language == "French":
        formated_language = "VF"
    elif language == "Original":
        formated_language = "VO"
    elif language == "DolbyCinema":
        formated_language = "Dolby"

    return formated_language
