package com.frankmoley.lil;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * The {@link President} provides a structured storage of a President of the United States of America
 * @author fpmoles.
 */
public class President {

    private String firstName;
    private String middleInitial;
    private String lastName;
    private String email;

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getMiddleInitial() {
        return middleInitial;
    }

    public void setMiddleInitial(String middleInitial) {
        this.middleInitial = middleInitial;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (o == null || getClass() != o.getClass()) return false;

        President president = (President) o;

        return new EqualsBuilder()
                .append(getFirstName(), president.getFirstName())
                .append(getMiddleInitial(), president.getMiddleInitial())
                .append(getLastName(), president.getLastName())
                .append(getEmail(), president.getEmail())
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37)
                .append(getFirstName())
                .append(getMiddleInitial())
                .append(getLastName())
                .append(getEmail())
                .toHashCode();
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this)
                .append("firstName", firstName)
                .append("middleInitial", middleInitial)
                .append("lastName", lastName)
                .append("email", email)
                .toString();
    }
}
