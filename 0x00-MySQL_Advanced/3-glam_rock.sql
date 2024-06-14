-- This script lists bands with Glam rock as their main style, ranked by longevity in years until 2022.
-- Column names are 'band_name' and 'lifespan'.


SELECT band_name, (IFNULL(split, 2022) - formed)
AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
