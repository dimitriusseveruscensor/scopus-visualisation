from scrape_article_xmldata import scrape
from xml_parser import parse
from co_autorships import autorships
from find_citations_MULTt import citations
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(description='Scopus pages scraper')
    parser.add_argument('apikey', help='your api key')
    parser.add_argument('startpage', help='which request page starts search', type=int)
    parser.add_argument('finishpage', help='which request page finishes search', type=int)
    parser.add_argument('subject', help='paper subject')
    parser.add_argument('dump_name', help='xml dump file name')
    parser.add_argument('dataset_name', help='csv dataset file name')
    parser.add_argument('--autorships', help='enable to extract autorships for papers', default=False, type=bool)
    parser.add_argument('--autorships_dump', help='autorships for papers dump file name')
    parser.add_argument('--citations', help='enable to extract citations for papers', default=False, type=bool)
    parser.add_argument('--citatons_dump', help='citations for papers dump file name')
    parser.add_argument('--citations_start', help='citations start point', type=int)
    parser.add_argument('--citations_finish', help='citations finish point', type=int)

    args = parser.parse_args()

    print('Start scraping')
    scrape(args.subject, args.startpage, args.finishpage, args.dump_name)
    print('Scraping finished. Start parsing dump')
    parse(args.dump_name, args.dataset_name)
    print('Finished parsing')

    if args.autorships:
        autorships(args.dataset_name, args.autorships_dump)

    if args.citations:
        citations(args.dataset_name, args.citations_dump, args.citations_start, args.citations_finish)
