--  lists all bands with Glam rock as their main style, ranked by their longevity
select band_name, (coalesce(split,extract(year from current_date)) - formed) as lifespan
from metal_bands
where style like "%Glam rock%";
