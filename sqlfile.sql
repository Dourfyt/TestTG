--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)

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
-- Name: tasks; Type: TABLE; Schema: public; Owner: testuser
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    created_at timestamp(0) without time zone DEFAULT now() NOT NULL,
    task text,
    user_id character varying(50)
);


ALTER TABLE public.tasks OWNER TO testuser;

--
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: testuser
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tasks_id_seq OWNER TO testuser;

--
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: testuser
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: testuser
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: testuser
--

COPY public.tasks (id, created_at, task, user_id) FROM stdin;
1	2024-05-01 00:20:13	sasd	\N
2	2024-05-01 00:20:53	fsad	\N
3	2024-05-01 00:30:47	Поставить чайник	\N
4	2024-05-02 00:05:42	a	1234746517
5	2024-05-02 00:10:05	a	1234746517
\.


--
-- Name: tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: testuser
--

SELECT pg_catalog.setval('public.tasks_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

