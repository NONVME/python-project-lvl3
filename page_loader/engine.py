from page_loader.file import write
from page_loader.html_builder import get_modified_page
from page_loader.http import get_data
from page_loader.url_formatter import to_dirname
from page_loader.url_formatter import get_domain, url_normalize


def download(url: str, dir_path: str) -> str:
    url = url_normalize(url)
    full_dirname = to_dirname(dir_path, url, '.html')
    page = get_data(url).text
    modified_page, original_links = get_modified_page(url, page, dir_path)
    write(modified_page, full_dirname)
    assets_dirname = to_dirname(dir_path, url, '_file')

    for link in original_links:
        domain_link = url_normalize(get_domain(url) + link)
        assets_full_dirname = to_dirname(assets_dirname, url, link,
                                         is_link=True)
        page = get_data(domain_link).content
        write(page, assets_full_dirname)

    return full_dirname
