CREATE TABLE "uploads" (
	"id" varchar PRIMARY KEY NOT NULL,
	"name" varchar NOT NULL,
	"remote_key" varchar NOT NULL,
	"remote_url" varchar NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "uploads_remote_key_unique" UNIQUE("remote_key")
);
