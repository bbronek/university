import org.junit.Before;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class InhabitantTest {

    Inhabitant inh = new Inhabitant();
    @Before
    public void setup() {
        inh.setImie("Janusz");
        inh.setNazwisko("Tracz");
        inh.setMiasto("Tulczyn");
        inh.setPesel("59081931121");
    }

    @Test
    public void setAndGetNameTest() {
        String expected = "Jan";
        inh.setImie(expected);

        assertEquals(expected, inh.getImie());
    }


}