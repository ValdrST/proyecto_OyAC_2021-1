LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY u_control IS
	PORT (
		inst : IN STD_LOGIC_VECTOR (15 DOWNTO 0);
		selregr : OUT STD_LOGIC_VECTOR (3 DOWNTO 0);
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
		seldirw : OUT STD_LOGIC_VECTOR (1 DOWNTO 0));
END u_control;

ARCHITECTURE Behavioral OF u_control IS
BEGIN
	PROCESS (inst)
	BEGIN
		CASE inst IS
			WHEN X"0086" => --LDAA(IMM)
				selregr <= X"0";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "100";
				seldir <= "00";
				selop <= X"4";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"1";
				selbranch <= "000";
				vf <= '1';
				selregw <= "001";
				memw <= '0';
				seldirw <= "00";

			WHEN X"00C6" => --LDAB(IMM)
				selregr <= X"0";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "100";
				seldir <= "00";
				selop <= X"4";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"1";
				selbranch <= "000";
				vf <= '1';
				selregw <= "100";
				memw <= '0';
				seldirw <= "00";

			WHEN X"00DE" => --LDX(DIR)
				selregr <= X"E";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "010";
				seldir <= "01";
				selop <= X"4";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"1";
				selbranch <= "000";
				vf <= '1';
				selregw <= "010";
				memw <= '0';
				seldirw <= "00";

			WHEN X"00AD" => --BRPARX
				selregr <= X"E";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "011";
				seldir <= "00";
				selop <= X"3";
				selresult <= "00";
				selc <= '0';
				cadj <= '0';
				selfalgs <= X"0";
				selbranch <= "010";
				vf <= '0';
				selregw <= "000";
				memw <= '0';
				seldirw <= "00";

			WHEN X"00AB" => --ADDA(ind,x)
				selregr <= X"6";
				sels1 <= '1';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "010";
				seldir <= "00";
				selop <= X"1";
				selresult <= "01";
				selc <= '0';
				cadj <= '0';
				selfalgs <= X"2";
				selbranch <= "000";
				vf <= '1';
				selregw <= "001";
				memw <= '0';
				seldirw <= "00";

			WHEN X"00E0" => --SUBB(ind,x)
				selregr <= X"2";
				sels1 <= '1';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "010";
				seldir <= "00";
				selop <= X"1";
				selresult <= "01";
				selc <= '0';
				cadj <= '0';
				selfalgs <= X"2";
				selbranch <= "000";
				vf <= '1';
				selregw <= "100";
				memw <= '0';
				seldirw <= "00";

			WHEN X"008C" => --CPX(IMM)
				selregr <= X"E";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "010";
				seldir <= "01";
				selop <= X"2";
				selresult <= "00";
				selc <= '1';
				cadj <= '1';
				selfalgs <= X"3";
				selbranch <= "000";
				vf <= '1';
				selregw <= "000";
				memw <= '0';
				seldirw <= "00";

			WHEN X"002F" => --BLE
				selregr <= X"0";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '1';
				seldato <= '0';
				selsrc <= "101";
				seldir <= "00";
				selop <= X"1";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"0";
				selbranch <= "100";
				vf <= '1';
				selregw <= "000";
				memw <= '0';
				seldirw <= "00";

			WHEN X"001B" => --ABA
				selregr <= X"1";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "001";
				seldir <= "00";
				selop <= X"1";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"2";
				selbranch <= "000";
				vf <= '1';
				selregw <= "001";
				memw <= '0';
				seldirw <= "00";

			WHEN X"0097" => --STAA(DIR)
				selregr <= X"4";
				sels1 <= '1';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "001";
				seldir <= "00";
				selop <= X"4";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"1";
				selbranch <= "000";
				vf <= '1';
				selregw <= "000";
				memw <= '1';
				seldirw <= "10";

			WHEN X"0020" => --BRA
				selregr <= X"0";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '1';
				seldato <= '0';
				selsrc <= "101";
				seldir <= "00";
				selop <= X"1";
				selresult <= "01";
				selc <= '1';
				cadj <= '0';
				selfalgs <= X"0";
				selbranch <= "000";
				vf <= '1';
				selregw <= "000";
				memw <= '0';
				seldirw <= "00";

			WHEN X"0080" => --INX
				selregr <= X"9";
				sels1 <= '0';
				sr <= '1';
				cin <= '0';
				sels2 <= '0';
				seldato <= '1';
				selsrc <= "001";
				seldir <= "00";
				selop <= X"1";
				selresult <= "01";
				selc <= '1';
				cadj <= '1';
				selfalgs <= X"C";
				selbranch <= "000";
				vf <= '1';
				selregw <= "010";
				memw <= '0';
				seldirw <= "00";

			WHEN X"0001" => --NOP
				selregr <= X"0";
				sels1 <= '0';
				sr <= '0';
				cin <= '0';
				sels2 <= '0';
				seldato <= '0';
				selsrc <= "000";
				seldir <= "00";
				selop <= X"0";
				selresult <= "00";
				selc <= '0';
				cadj <= '0';
				selfalgs <= X"0";
				selbranch <= "000";
				vf <= '1';
				selregw <= "000";
				memw <= '0';
				seldirw <= "00";
			WHEN OTHERS => -- NOP a lo que no exista
				selregr <= X"0";
				sels1 <= '0';
				sr <= '0';
				cin <= '0';
				sels2 <= '0';
				seldato <= '0';
				selsrc <= "000";
				seldir <= "00";
				selop <= X"0";
				selresult <= "00";
				selc <= '0';
				cadj <= '0';
				selfalgs <= X"0";
				selbranch <= "000";
				vf <= '1';
				selregw <= "000";
				memw <= '0';
				seldirw <= "00";
		END CASE;
	END PROCESS;
END Behavioral;