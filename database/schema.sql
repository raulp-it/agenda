--
-- PostgreSQL database dump
--

\restrict GClQkm3bi1bvteZ5mt9SuFaHxWWcBrr45wb8cZ1UfmBk1PK15p0YNfLg8tuzvfG

-- Dumped from database version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: age_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.age_base (
    id integer NOT NULL,
    codigo character varying(20) NOT NULL,
    apellido character varying(150) NOT NULL,
    nombre character varying(50),
    domicilio character varying(80),
    cp character varying(4),
    email character varying(50),
    activo boolean DEFAULT true NOT NULL,
    fecha_alta timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    telefono character varying(20),
    localidad character varying(50)
);


ALTER TABLE public.age_base OWNER TO postgres;

--
-- Name: TABLE age_base; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.age_base IS 'Agenda reimplementada en Python a partir del proyecto original en DBase III Plus (1995)';


--
-- Name: agenda_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.agenda_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.agenda_id_seq OWNER TO postgres;

--
-- Name: agenda_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.agenda_id_seq OWNED BY public.age_base.id;


--
-- Name: age_base id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.age_base ALTER COLUMN id SET DEFAULT nextval('public.agenda_id_seq'::regclass);


--
-- Name: age_base age_base_codigo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.age_base
    ADD CONSTRAINT age_base_codigo_key UNIQUE (codigo);


--
-- Name: age_base age_base_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.age_base
    ADD CONSTRAINT age_base_pkey PRIMARY KEY (id);


--
-- Name: TABLE age_base; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.age_base TO agenda_usr;


--
-- Name: SEQUENCE agenda_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.agenda_id_seq TO agenda_usr;


--
-- PostgreSQL database dump complete
--

\unrestrict GClQkm3bi1bvteZ5mt9SuFaHxWWcBrr45wb8cZ1UfmBk1PK15p0YNfLg8tuzvfG

