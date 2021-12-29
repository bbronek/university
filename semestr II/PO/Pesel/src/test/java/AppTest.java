import jdk.jfr.Description;
import org.junit.Ignore;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class AppTest {


    @Test()
    public void shouldReturnPeselLengthExcpetion()  {
         Exception exception = assertThrows(PeselException.class, () -> {
             App.checkPesel("345");
         });

        String expectedMessage = "CustomException: Nie poprawna dlugosc peselu";
        String actualMessage = exception.toString();

        assertEquals(expectedMessage, actualMessage);
    }

    @Ignore("Remove to run tests")
    @Test
    public void shouldReturnCOntrolDigitExcpetion()  {
         Exception exception = assertThrows(PeselException.class, () -> {
             App.checkPesel("12345678912");
         });

        String expectedMessage = "CustomException: Nie poprawna cyfra kontrolna";
        String actualMessage = exception.toString();

        assertEquals(expectedMessage, actualMessage);
    }

    @Test
    @Description("Function should return false when in list exists person with same pesel")
    public void modifyDataTest() {
        boolean expected = false;
        Inhabitant inh = new Inhabitant();

        inh.setMiasto("Warszawa");
        inh.setImie("Jan");
        inh.setNazwisko("kowalski");
        inh.setPesel("63120792893");

        List<Inhabitant> listInhabitants = new ArrayList<>();
        listInhabitants.add(inh);
        inh.setImie("Tomasz");
        listInhabitants.add(inh);

        assertEquals(expected, App.modifyData(inh, listInhabitants));
    }


}