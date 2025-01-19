import java.util.*;

class ProductItem {
    private final int id; // Make id final
    private final float price; // Make price final

    public ProductItem(int id, float price) {
        this.id = id;
        this.price = price;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", PRICE: " + price;
    }

    public float getPrice() {
        return price;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        ProductItem other = (ProductItem) obj;
        return id == other.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id); // Implement hashCode
    }
}

class ShoppingCart {
    private final int custid; // Make custid final
    private final ArrayList<ProductItem> items; // Make items final

    public ShoppingCart(int custid) {
        this.custid = custid;
        this.items = new ArrayList<>();
    }

    public void addItem(ProductItem item) {
        items.add(item);
    }

    public void removeItem(ProductItem item) {
        items.remove(item);
    }

    public void doPayment() {
        float total = 0.0f;
        for (ProductItem item : items) {
            total += item.getPrice();
        }
        System.out.println("Total Price: " + total);
    }

    public void displayItems() {
        System.out.println("Customer ID: " + custid); // Use custid
        for (ProductItem item : items) {
            System.out.println(item.toString());
        }
    }
}

public class AggregationRelationship {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart(1);
        ProductItem item1 = new ProductItem(1, 200);
        cart.addItem(item1);
        ProductItem item2 = new ProductItem(2, 300);
        cart.addItem(item2);
        ProductItem item3 = new ProductItem(3, 1300);
        cart.addItem(item3);
        ProductItem item4 = new ProductItem(4, 1000);
        cart.addItem(item4);
        cart.removeItem(item3);
        System.out.println("Items in cart:");
        cart.displayItems();
        System.out.println();
        cart.doPayment();
        System.out.println();
    }
}