--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

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
-- Name: admin; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin (
    admin_id integer NOT NULL,
    admin_name character varying,
    password character varying
);


--
-- Name: admin_admin_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_admin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_admin_id_seq OWNED BY public.admin.admin_id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: symptom; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.symptom (
    symptom_id integer NOT NULL,
    title character varying,
    description character varying,
    description_url character varying
);


--
-- Name: symptom_symptom_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.symptom_symptom_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: symptom_symptom_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.symptom_symptom_id_seq OWNED BY public.symptom.symptom_id;


--
-- Name: admin admin_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin ALTER COLUMN admin_id SET DEFAULT nextval('public.admin_admin_id_seq'::regclass);


--
-- Name: symptom symptom_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.symptom ALTER COLUMN symptom_id SET DEFAULT nextval('public.symptom_symptom_id_seq'::regclass);


--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.admin (admin_id, admin_name, password) FROM stdin;
18	test11	$2b$12$MwsbHMjIG.t1i6Y8PFzgduPxM7jxg2Kz5IswrUaF8Y1ztUTnEwBMO
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alembic_version (version_num) FROM stdin;
8d0965dd3d25
\.


--
-- Data for Name: symptom; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.symptom (symptom_id, title, description, description_url) FROM stdin;
10	Gum Problems	Gum infections and abscess	https://www.mouthhealthy.org/all-topics-a-z/abscess
12	Gum Problems	Common Gum diseases |Periodontitis	https://www.mouthhealthy.org/all-topics-a-z/gum-disease
8	Tooth Pain	Mouth Sores	https://www.mouthhealthy.org/all-topics-a-z/mouth-sores
3	Tooth Problems	Missing Teeth	https://www.mouthhealthy.org/all-topics-a-z/missing-teeth
2	Tooth Problems	Cavity or Tooth Decay	https://www.mouthhealthy.org/all-topics-a-z/cavities
22	Gum Problems	Red Bleeding Gums	https://www.mouthhealthy.org/all-topics-a-z/bleeding-gums
5	Tooth Pain	Jaw Pain	https://www.mouthhealthy.org/all-topics-a-z/jaw-pain
7	Tooth Pain	Clenching & Grinding	https://www.mouthhealthy.org/all-topics-a-z/teeth-grinding
13	Dental Emergencies	Broken or Cracked Teeth or Lip & Tongue Biting	https://www.mouthhealthy.org/dental-care-concerns/dental-emergencies
28	Tooth Problems	Bad Breath	https://www.mouthhealthy.org/all-topics-a-z/bad-breath
29	Tooth Pain	Hot & Cold Sensitivity	https://www.mouthhealthy.org/all-topics-a-z/sensitive-teeth
34	Demo	Milcah my 🌍	https://www.google.com/
4	Tooth Problems	Baby Teething	https://www.mouthhealthy.org/all-topics-a-z/teething
\.


--
-- Name: admin_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.admin_admin_id_seq', 18, true);


--
-- Name: symptom_symptom_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.symptom_symptom_id_seq', 34, true);


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (admin_id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: symptom symptom_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.symptom
    ADD CONSTRAINT symptom_pkey PRIMARY KEY (symptom_id);


--
-- PostgreSQL database dump complete
--

