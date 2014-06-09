from sys import argv

def create_dict(text_file):

    restaurant_dict = {}

    for line in text_file:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        rating = int(rating)

        restaurant_dict[restaurant] = rating

    return restaurant_dict

def sort_dict(restaurant_dict):

    sorted_keys = sorted(restaurant_dict.keys())

    for key in sorted_keys:
        print "Restaurant %s is rated at %d." % (key, restaurant_dict[key])

def main():

    filename = argv[1]
    my_file = open(filename)

    restaurant_dict = create_dict(my_file)
    
    sort_dict(restaurant_dict)

if __name__ == "__main__":
    main()