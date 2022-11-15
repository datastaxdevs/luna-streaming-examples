import java.sql.*;

class PrestoExample {
  public static void main(String[] args) {
    try {
      Connection conn = DriverManager.getConnection("jdbc:presto://localhost:8090/pulsar?user=test");
      System.out.println("Connection established......");

      Statement stmt = conn.createStatement();

      try {
        ResultSet rs = stmt.executeQuery("select * from pulsar.\"public/default\".mytopic limit 10");
        while(rs.next()) {
            String str = rs.getString(1);
            System.out.println(String.format("%s", str));
        }
      }
      finally {
        stmt.close();
        conn.close();
      }
    }
    catch (Exception e) {
      e.printStackTrace();
    }
  }
}