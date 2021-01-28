LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY u_anticipaciones IS
    PORT (
        selregR : IN STD_LOGIC_VECTOR (2 DOWNTO 0);
        selregW : IN STD_LOGIC_VECTOR (2 DOWNTO 0);
        selB : OUT STD_LOGIC := '0';
        selA : OUT STD_LOGIC := '0'
    );
END u_anticipaciones;

ARCHITECTURE Behavioral OF u_anticipaciones IS
BEGIN
    PROCESS (selregR, selregW)
    BEGIN
        IF selregR = x"1" AND selregW = x"1" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"1" AND selregW = X"4" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"2" AND selregW = X"4" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"2" AND selregW = X"2" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"3" AND selregW = X"4" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"3" AND selregW = X"3" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"4" AND selregW = X"1" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"5" AND selregW = X"4" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"6" AND selregW = X"1" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"6" AND selregW = X"2" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"7" AND selregW = X"1" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"7" AND selregW = X"3" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"8" AND selregW = X"5" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"9" AND selregW = X"2" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"A" AND selregW = X"3" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"B" AND selregW = X"6" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"C" AND selregW = X"1" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"C" AND selregW = X"6" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"D" AND selregW = X"4" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"D" AND selregW = X"6" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"E" AND selregW = X"2" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"E" AND selregW = X"6" THEN
            selA <= '0';
            selB <= '1';
        ELSIF selregR = X"F" AND selregW = X"3" THEN
            selA <= '1';
            selB <= '0';
        ELSIF selregR = X"F" AND selregW = X"6" THEN
            selA <= '0';
            selB <= '1';
        ELSE
            selA <= '0';
            selB <= '0';
        END IF;
    END PROCESS;
END Behavioral;