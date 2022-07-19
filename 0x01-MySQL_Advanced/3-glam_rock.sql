-- Column names must be: band_name and lifespan (in years)
-- You should use attributes formed and split for computing the lifespan
-- Your script can be executed on any database
-- You can use any database

SELECT band_name, IFNull(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style Like '%Glam rock%'
ORDER BY lifespan DESC;
