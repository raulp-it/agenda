-- ======================================================
-- Agenda - DBase III a Python
-- Estructura de la base de datos
-- ======================================================

CREATE TABLE age_base (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    codigo VARCHAR(20) NOT NULL UNIQUE,
    apellido VARCHAR(150) NOT NULL,
    nombre VARCHAR(50),
    domicilio VARCHAR(80),
    cp VARCHAR(4),
    email VARCHAR(50),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_alta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    telefono VARCHAR(20),
    localidad VARCHAR(50)
);

GRANT ALL PRIVILEGES ON TABLE age_base TO agenda_usr;
COMMENT ON TABLE age_base IS
'Agenda reimplementada en Python a partir del proyecto original en DBase III Plus (1995)';
