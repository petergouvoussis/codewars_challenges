SELECT top.id AS id,
       top.heads AS heads,
       bottom.legs AS legs,
       top.arms AS arms,
       bottom.tails AS tails,
       CASE WHEN (top.heads > top.arms OR bottom.tails > bottom.legs)
             THEN 'BEAST'
             ELSE 'WEIRDO' END AS species
FROM top_half AS top
JOIN bottom_half AS bottom ON top.id = bottom.id
ORDER BY species;
