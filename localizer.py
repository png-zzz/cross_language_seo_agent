from openai import OpenAI
client = OpenAI(api_key='YOUR_OPENAI_API_KEY')

def localize_content(text, target_language='zh', seo_keywords=None):
    prompt = f"""请将以下商品文案翻译并本土化为 {target_language}：
{text}
请保证：
1. 语言自然流畅
2. 融入以下 SEO 关键词：{', '.join(seo_keywords) if seo_keywords else '无'}
3. 保留商品核心卖点
输出完整可发布文案
"""
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role':'user','content':prompt}],
        max_tokens=600
    )
    return response.choices[0].message['content'].strip()

def generate_multilingual_content(product, target_languages, seo_keywords_map):
    localized_results = {}
    combined_text = f"{product['title']}\n{product['description']}")
    for lang in target_languages:
        seo_keywords = seo_keywords_map.get(lang, [])
        localized_results[lang] = localize_content(combined_text, lang, seo_keywords)
    return localized_results
