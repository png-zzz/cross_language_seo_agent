import product_scraper
import localizer

if __name__ == '__main__':
    product_url = 'https://example.com/product/12345'
    target_languages = ['zh', 'en', 'es']
    seo_keywords_map = {
        'zh': ['夏季连衣裙', '轻薄透气'],
        'en': ['summer dress', 'light breathable'],
        'es': ['vestido de verano', 'ligero y transpirable']
    }

    product = product_scraper.fetch_product_data(product_url)
    content = localizer.generate_multilingual_content(product, target_languages, seo_keywords_map)

    for lang, text in content.items():
        print(f'===== {lang.upper()} 本土化文案 =====')
        print(text)
