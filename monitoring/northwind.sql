-- Création de la table "products"
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

-- Insertion de données
INSERT INTO products (name, price) VALUES
('Produit A', 10.99),
('Produit B', 15.49),
('Produit C', 8.75);
