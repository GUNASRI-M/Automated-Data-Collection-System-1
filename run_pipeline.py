from scraper.collect import collect

from scraper.parse import parse

from scraper.save import save


def run():

    links = collect()

    for link in links:

        try:

            data = parse(link)

            save(data)

            print(
                "saved"
            )

        except Exception as e:

            print(
                e
            )


run()

print(
    "DONE"
)