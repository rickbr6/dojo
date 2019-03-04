USE sakila;
-- 1)
SELECT customer.first_name, 
       customer.last_name,
       customer.email,
       address.address,
       address.address2,
       address.postal_code,
       city.city,
       city.city_id,
       city.country_id
FROM customer
JOIN address on customer.address_id = address.address_id
JOIN city on address.city_id = city.city_id
WHERE city.city_id = 312;

-- 2)
SELECT film.title, 
    film.description, 
    film.release_year, 
    film.rating, 
    film.special_features,
    category.name
FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on  film_category.category_id = category.category_id
WHERE category.category_id = 5;

-- 3)
USE sakila;
SELECT film.title,
    film.description,
    film.release_year,
    actor.first_name,
    actor.actor_id,
    actor.last_name
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- 4)
SELECT customer.first_name,
    customer.last_name,
    customer.email,
    address.address,
    address.address2,
    address.postal_code,
    city.city  
FROM customer
JOIN address on customer.address_id = address.address_id
JOIN city on address.city_id = city.city_id
WHERE customer.store_id = 1 and
	address.city_id in (1, 42, 312, 459);

-- 5)
SELECT film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 15 and film.rating = "G" and film.special_features LIKE '%behind%';


-- 6)
SELECT film.film_id,
    film.title,
    film.description,
    actor.actor_id,
    actor.first_name AS actor_first_name,
    actor.last_name AS actor_last_name
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- 7)
SELECT film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features,
    film.rental_rate,
    category.name
FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 and category.category_id = 7;

-- 8)
SELECT film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features,
    category.name,
    actor.first_name,
    actor.last_name
FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
JOIN film_actor on film_actor.film_id = film.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE actor.last_name = "Kilmer" and actor.first_name = "Sandra" and category.name = "Action";