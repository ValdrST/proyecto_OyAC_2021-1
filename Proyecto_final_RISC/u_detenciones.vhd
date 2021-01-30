LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY u_detenciones IS
	PORT (
		selsrcc : IN STD_LOGIC_VECTOR (2 DOWNTO 0);
		memWc : IN STD_LOGIC;
		Branch : IN STD_LOGIC;
		ifidwrite : OUT STD_LOGIC := '1';
		PCWrite : OUT STD_LOGIC := '1';
		selctrl : OUT STD_LOGIC := '0';
		--burbuja
		selregr2 : OUT STD_LOGIC_VECTOR (3 DOWNTO 0);
		sels1 : OUT STD_LOGIC;
		sr : OUT STD_LOGIC;
		cin : OUT STD_LOGIC;
		sels2 : OUT STD_LOGIC;
		seldato : OUT STD_LOGIC;
		selsrc : OUT STD_LOGIC_VECTOR (2 DOWNTO 0);
		seldir : OUT STD_LOGIC_VECTOR(1 DOWNTO 0);
		selop : OUT STD_LOGIC_VECTOR (3 DOWNTO 0);
		selresult : OUT STD_LOGIC_VECTOR (1 DOWNTO 0);
		selc : OUT STD_LOGIC;
		cadj : OUT STD_LOGIC;
		selfalgs : OUT STD_LOGIC_VECTOR (3 DOWNTO 0);
		selbranch : OUT STD_LOGIC_VECTOR (2 DOWNTO 0);
		vf : OUT STD_LOGIC;
		selregw : OUT STD_LOGIC_VECTOR (2 DOWNTO 0);
		memw : OUT STD_LOGIC;
		seldirw : OUT STD_LOGIC_VECTOR (1 DOWNTO 0);
		selD : OUT STD_LOGIC := '0';
		EXFlush : OUT STD_LOGIC := '0');
END u_detenciones;

ARCHITECTURE Behavioral OF u_detenciones IS
BEGIN
	PROCESS (selsrcc, memWc)
	BEGIN
		--burbuja
		selregr2 <= "0000";
		sels1 <= '0';
		sr <= '0';
		cin <= '0';
		sels2 <= '0';
		seldato <= '0';
		selsrc <= "000";
		seldir <= "00";
		selop <= "0000";
		selresult <= "00";
		selc <= '0';
		cadj <= '0';
		selfalgs <= "0000";
		selbranch <= "000";
		vf <= '1';
		selregw <= "000";
		memw <= '0';
		seldirw <= "00";
		
		IF (selsrcc = X"2" OR selsrcc = X"4" OR selsrcc = X"6") AND memWc = '1' AND Branch = '0' THEN
			PCWrite <= '0';
			ifidwrite <= '0';
			selD <= '1';
			selctrl <= '1';
			EXFlush <= '0';
		ELSIF selsrcc = X"4" AND memWc = '1' THEN
			PCWrite <= '1';
			ifidwrite <= '1';
			selD <= '0';
			selctrl <= '1';
			EXFlush <= '1';
		ELSIF selsrcc = X"2" AND memWc = '1' THEN
			PCWrite <= '0';
			ifidwrite <= '0';
			selD <= '1';
			selctrl <= '1';
			EXFlush <= '0';
		ELSIF selsrcc = X"4" AND memWc = '1' THEN
			PCWrite <= '0';
			ifidwrite <= '0';
			selD <= '1';
			selctrl <= '1';
			EXFlush <= '0';
		ELSIF selsrcc = X"6" AND memWc = '1' THEN
			PCWrite <= '0';
			ifidwrite <= '0';
			selD <= '1';
			selctrl <= '1';
			EXFlush <= '0';
		ELSIF selsrcc = X"2" AND memWc = '0' THEN
			PCWrite <= '1';
			ifidwrite <= '1';
			selD <= '0';
			selctrl <= '0';
			EXFlush <= '0';
		ELSIF selsrcc = X"4" AND memWc = '0' THEN
			PCWrite <= '1';
			ifidwrite <= '1';
			selD <= '0';
			selctrl <= '0';
			EXFlush <= '0';
		ELSIF selsrcc = X"6" AND memWc = '0' THEN
			PCWrite <= '1';
			ifidwrite <= '1';
			selD <= '0';
			selctrl <= '0';
			EXFlush <= '0';
		ELSE
			PCWrite <= '1';
			ifidwrite <= '1';
			selD <= '0';
			selctrl <= '0';
			EXFlush <= '0';
		END IF;
	END PROCESS;
END Behavioral;