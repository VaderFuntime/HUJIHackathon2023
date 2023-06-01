import generate_confession
import conf_to_image


def generate_conf_and_img():
    eng_conf, heb_conf = generate_confession.generate_confession_eng_heb()
    img_url = conf_to_image.create_image(eng_conf)
    return heb_conf, img_url


if __name__ == '__main__':
    conf, img_url = generate_conf_and_img()
    print(conf)
    print(img_url)
