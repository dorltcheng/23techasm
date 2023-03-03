SELECT owner.owner_id, 
	owner_name, 
    COUNT(DISTINCT category_id) AS different_category_count
FROM article 
JOIN category_article_mapping 
	ON article.article_id = category_article_mapping.article_id
JOIN owner 
	ON owner.owner_id = article.owner_id
GROUP BY owner.owner_id
ORDER BY different_category_count DESC;