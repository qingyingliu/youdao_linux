DROP TABLE IF EXISTS word;
DROP TABLE IF EXISTS count;

CREATE TABLE word (
  word TEXT PRIMARY KEY,
  phonetic_symbol TEXT,
  word_attr TEXT,
  meanings TEXT NOT NULL,
  en_sentence1 TEXT,
  cn_sentence1 TEXT,
  en_sentence2 TEXT,
  cn_sentence2 TEXT,
  en_sentence3 TEXT,
  cn_sentence3 TEXT
); 

CREATE TABLE count(
    word TEXT PRIMARY KEY,
    times INTEGER NOT NULL DEFAULT 0
);