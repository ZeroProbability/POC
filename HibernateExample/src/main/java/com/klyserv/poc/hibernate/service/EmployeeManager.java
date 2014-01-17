package com.klyserv.poc.hibernate.service;

import java.util.List;

import com.klyserv.poc.hibernate.entity.EmployeeEntity;

public interface EmployeeManager {
	public void addEmployee(EmployeeEntity employee);

	public List<EmployeeEntity> getAllEmployees();

	public void deleteEmployee(Integer employeeId);

}
