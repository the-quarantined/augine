from unicodedata import category
from django.shortcuts import render
# Create your views here.
from .models import Product
from django.views.generic import CreateView
from .forms import ProductForm
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import extcolors
from colormap import rgb2hex
from django.urls import reverse

# logic and functions to be written here


def image(request):

    #   so this is where i am right now
    # we have to figure out a way
    # we basically fill a form at this page
    # the data send as post request is nothing but a string and that string is inputted to the next page
    # the next page is nothing but the categories page
    # on the categories page few things would be accessible to us
    # the string accessible to us would help us in getting the most prominent color of that image
    # now on the categories page all the data would be avaialble to us and we can do whatever we want to do
    # all the products with the color will be displayed

    return render(request, 'image.html')


def find_color_name(a, b, c):
    if a >= 0 and a <= 360 and b >= 0 and b <= 1 and c <= 0.1:
        return 10
        # print("black")
    # black
    elif a >= 0 and a <= 360 and b <= 0.15 and c >= 0.65:
        return 0
        # print("white")
    # white
    elif a >= 0 and a <= 360 and b <= 0.15 and c >= 0.1 and c <= 0.65:
        return 11
        # print("gray")
    # gray
    elif (a >= 351 or a <= 11) and b >= 0.5 and c >= 0.1:
        return 7
        # print("red")
    # red
    elif (a >= 351 or a <= 11) and b <= 0.5 and c >= 0.1:
        return 6
        # print("pink")
    # pink
    elif a >= 310 and a <= 351 and b >= 0.15 and c >= 0.1:
        return 6
        # print("pink")
    # pink2
    elif a <= 45 and a >= 11 and b >= 0.15 and c >= 0.75:
        return 9
        # print("orange")
    # orange
    elif a <= 45 and a >= 11 and b >= 0.15 and c <= 0.75 and c >= 0.1:
        return 8
        # print("brown")
    # brown
    elif a >= 45 and a <= 64 and b >= 0.15 and c >= 0.1:
        return 1
        # print("yellow")
    # yellow
    elif a >= 64 and a <= 150 and b >= 0.15 and c >= 0.1:
        return 2
        # print("green")
    # green
    elif a >= 150 and a <= 180 and b >= 0.15 and c >= 0.1:
        return 3
        # print("blue green")
    # blue green
    elif a >= 180 and a <= 255 and b >= 0.15 and c >= 0.1:
        return 4
        # print("blue")
    # blue
    elif a >= 255 and a <= 310 and b >= 0.5 and c >= 0.1:
        return 5
        # print("purple")
    # purple
    elif a >= 255 and b <= 310 and b >= 0.15 and b <= 0.50 and c >= 0.1:
        return 5
        # print("purple")
    else:
        return -1
    # light purple
    return


def rgb2hsv(r, g, b):
    # Normalize R, G, B values
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    # h, s, v = hue, saturation, value
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    difference = max_rgb-min_rgb
    # if max_rgb and max_rgb are equal then h = 0
    if max_rgb == min_rgb:
        h = 0
    # if max_rgb==r then h is computed as follows
    elif max_rgb == r:
        h = (60 * ((g - b) / difference) + 360) % 360
    # if max_rgb==g then compute h as follows
    elif max_rgb == g:
        h = (60 * ((b - r) / difference) + 120) % 360
    # if max_rgb=b then compute h
    elif max_rgb == b:
        h = (60 * ((r - g) / difference) + 240) % 360
    # if max_rgb==zero then s=0
    if max_rgb == 0:
        s = 0
    else:
        s = (difference / max_rgb) * 100
    # compute v
    v = max_rgb * 100
    # return rounded values of H, S and V
    return tuple(map(round, (h, s, v)))


def hex2rgb(hex_value):
    h = hex_value.strip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb


def color_to_df(input):
    colors_pre_list = str(input).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]
    # convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                           int(i.split(", ")[1]),
                           int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]

    df = pd.DataFrame(zip(df_color_up, df_percent),
                      columns=['c_code', 'occurence'])
    return df


def exact_color(input_image, resize, tolerance, zoom):   # use this fuction to find color
    # background
    bg = 'bg.png'
    fig, ax = plt.subplots(figsize=(192, 108), dpi=10)
    fig.set_facecolor('white')
    plt.savefig(bg)
    plt.close(fig)
    # resize
    output_width = resize
    img = Image.open(input_image)
    if img.size[0] >= resize:
        wpercent = (output_width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((output_width, hsize), Image.ANTIALIAS)
        resize_name = 'resize_' + input_image
        img.save(resize_name)
    else:
        resize_name = input_image
    # TILL HERE WE HAVE ONLY RESIZED OUR ORIGINAL IMAGE
    # crate dataframe
    img_url = resize_name
    colors_x = extcolors.extract_from_path(
        img_url, tolerance=tolerance, limit=13)
    df_color = color_to_df(colors_x)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # print(df_color)
    list_color = list(df_color['c_code'])
    temp = []
    for color in list_color:
        help = hex2rgb(color)
        # i am able to get the hsv for this color
        final = rgb2hsv(help[0], help[1], help[2])
        a = final[0]
        b = float(final[1]/100)
        c = float(final[2]/100)
        # print(a, b, c)
        t = find_color_name(a, b, c)
        if t not in temp:
            temp.append(t)
    print(temp)
    return


def home(request):
    return render(request, 'home.html')


class AddProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'addProd.html'

    def get_absolute_url(self):  # new
        return reverse('addProd', args=[str(self.id)])
    # if request.method == "POST":
    #     prodname = request.POST.get('prodname')
    #     price = request.POST.get('price')
    #     category = request.POST.get('category')
    #     desc = request.POST.get('description')
    #     # file = request.POST.get('image')
    #     prod = Product(name=prodname, price=price,
    #                    category=category, desc=desc)
    #     prod.save()
    # return render(request, 'addProd.html')


def showCategories(request):
    allProds = Product.objects.all()
    category = {}
    for prod in allProds:
        if prod.category in category:
            category[prod.category].append(prod.name)
        else:
            print(type(prod.category))
            category[prod.category] = []
            category[prod.category].append(prod.name)
    # print(type(category))
    return render(request, 'categories.html', {'category': category})
