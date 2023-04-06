--  lists all bands with Glam rock as their main style, ranked by their longevity
select band_name, (ifnull(split, '2020') - formed) as lifespan
from metal_bands
where find_in_set('Glam rock', ifnull(style, "")) > 0
order by lifespan desc;
