-- dbscript\\table.sql
-- 동적 웹 크롤링에서 여행지 검색 결과 저장용 테이블 생성 스크립트

DROP TABLE TOUR CASCADE CONSTRAINTS;

CREATE TABLE TOUR(
    RANK    VARCHAR2(100),
    NAME    VARCHAR2(100),
    DESCRIPTION     VARCHAR2(2000),
    CATEGORY    VARCHAR2(100)
);

COMMIT;