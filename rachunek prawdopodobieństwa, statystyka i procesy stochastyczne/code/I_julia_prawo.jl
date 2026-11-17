using Random, Statistics

rng = MersenneTwister(104)
p = 0.35
for n in (10, 100, 1000, 10000)
    X = rand(rng, n) .< p
    println("n = $n, srednia = $(mean(X))")
end
# Pojedynczy wynik jest losowy; twierdzenie dotyczy n -> infinity.
