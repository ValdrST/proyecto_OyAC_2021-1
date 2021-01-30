-- memoria de solo lectura

LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY memoria_inst IS
	PORT (
		direccion : IN STD_LOGIC_VECTOR (15 DOWNTO 0);
		datos : OUT STD_LOGIC_VECTOR (31 DOWNTO 0));
END memoria_inst;

ARCHITECTURE Behavioral OF memoria_inst IS

	TYPE memory IS ARRAY(0 TO 50) OF STD_LOGIC_VECTOR(31 DOWNTO 0);
	SIGNAL memoria : memory;
BEGIN
	--		memoria(0) <= x"00860000"; --	LDAA	#$0000	(A <- 0)
	--		memoria(1) <= x"00A50001"; --	LDAB	#$0002	(B <- 2)
	--		memoria(2) <= x"00010000"; --	NOP				(Nops de salto)
	--		memoria(3) <= x"00010000"; --	NOP
	--		memoria(4) <= x"001B0000"; --	ABA			(A <- A + B)
	--		memoria(5) <= x"005C0000"; --	INCB	#$0002	(Salto a dir 2)
	--		memoria(6) <= x"007E0002"; --	JMP
	--		memoria(7) <= x"00010000"; --	NOP				(Nops de salto)
	--		memoria(8) <= x"00010000"; --	NOP

	--	attribute ram_init_file : string;
	--   attribute ram_init_file of mem : signal is "mem_prog.mif";
	memoria(0) <=  x"00CE0003";
	memoria(1) <=  x"00860020";
	memoria(2) <=  x"00C600FF";
	memoria(3) <=  x"00A50000";
	memoria(4) <=  x"00250003";
	memoria(5) <=  x"00010000";
	memoria(6) <=  x"00010000";
	memoria(7) <=  x"007E0015";
	memoria(8) <=  x"00AB0000";
	memoria(9) <=  x"00800000";
	memoria(10) <=  x"008C0008";
	memoria(11) <=  x"00270004";
	memoria(12) <=  x"00010000";
	memoria(14) <=  x"00010000";
	memoria(15) <=  x"00730003";
	memoria(16) <=  x"00010000";
	memoria(17) <=  x"00010000";
	memoria(18) <=  x"0073001F";
	memoria(19) <=  x"00010000";
	memoria(20) <=  x"00010000";
	memoria(21) <=  x"00E00000";
	memoria(22) <=  x"00800000";
	memoria(23) <=  x"008C0008";
	memoria(24) <=  x"00270000";
	memoria(25) <=  x"00010000";
	memoria(26) <=  x"00010000";
	memoria(27) <=  x"007E0003";
	memoria(28) <=  x"00010000";
	memoria(29) <=  x"00010000";
	memoria(31) <=  x"00AD0000";
	memoria(32) <=  x"007E0000";
	memoria(33) <=  x"00010000";
	memoria(34) <=  x"00010000";

	PROCESS (direccion)
	BEGIN
		datos <= memoria(conv_integer(unsigned(direccion)));
	END PROCESS;
END Behavioral;